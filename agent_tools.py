#!/usr/bin/env python3
"""
AI Agent Toolkit — Essential CLI tools for AI agent developers
==============================================================
A collection of production-ready utilities for building AI agents.
Zero dependencies beyond Python stdlib. Works on any OS.

Commands:
  web-fetch    - Fetch and extract clean text from any URL
  file-watch   - Watch directories for changes and trigger actions  
  cron-gen     - Generate crontab entries from natural language
  json-query   - Query JSON files with simple path expressions
  batch-run    - Run commands in parallel with rate limiting
  log-parse    - Parse and filter structured logs
"""

import sys, os, json, re, time, argparse
import urllib.request, urllib.error
from pathlib import Path
from html.parser import HTMLParser

# ─── Web Fetch ───────────────────────────────────────────
class TextExtractor(HTMLParser):
    """Extract clean text from HTML, stripping tags and scripts"""
    def __init__(self):
        super().__init__()
        self.text = []
        self.skip = False
        
    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style', 'noscript'):
            self.skip = True
            
    def handle_endtag(self, tag):
        if tag in ('script', 'style', 'noscript'):
            self.skip = False
        if tag in ('p', 'br', 'div', 'li', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
            self.text.append('\n')
            
    def handle_data(self, data):
        if not self.skip:
            text = data.strip()
            if text:
                self.text.append(text + ' ')

def web_fetch(url, output=None, selector=None):
    """Fetch a URL and extract readable text"""
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'AI-Agent-Toolkit/1.0'})
        html = urllib.request.urlopen(req, timeout=15).read().decode('utf-8', errors='replace')
        
        extractor = TextExtractor()
        extractor.feed(html)
        text = ''.join(extractor.text)
        
        # Clean up whitespace
        text = re.sub(r'\n\s*\n', '\n\n', text)
        text = re.sub(r' +', ' ', text)
        
        if output:
            Path(output).write_text(text.strip())
            print(f"Saved {len(text)} chars to {output}")
        else:
            print(text.strip()[:5000])
        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

# ─── JSON Query ──────────────────────────────────────────
def json_query(filepath, query):
    """Query JSON with dot-notation path: data.users.0.name"""
    data = json.loads(Path(filepath).read_text())
    for key in query.split('.'):
        if isinstance(data, list):
            try:
                data = data[int(key)]
            except (ValueError, IndexError):
                data = [item.get(key) if isinstance(item, dict) else None for item in data]
        elif isinstance(data, dict):
            data = data.get(key)
        else:
            print("null")
            return 1
    print(json.dumps(data, indent=2, ensure_ascii=False) if not isinstance(data, str) else data)
    return 0

# ─── File Watch ──────────────────────────────────────────
def file_watch(directory, command, pattern="*", interval=5):
    """Watch a directory and run command on changes"""
    import hashlib
    dirpath = Path(directory)
    if not dirpath.exists():
        print(f"Directory {directory} does not exist", file=sys.stderr)
        return 1
    
    print(f"Watching {directory} (pattern: {pattern}, interval: {interval}s)")
    prev = {}
    
    try:
        while True:
            current = {}
            for f in dirpath.rglob(pattern):
                if f.is_file():
                    current[str(f)] = f.stat().st_mtime
            
            changed = [f for f in current if f not in prev or current[f] != prev[f]]
            if changed:
                print(f"\n[{time.strftime('%H:%M:%S')}] Changed: {len(changed)} files")
                for f in changed[:5]:
                    print(f"  {f}")
                os.system(command)
            
            prev = current
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nStopped.")
    return 0

# ─── Main ────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description='AI Agent Toolkit')
    sub = parser.add_subparsers(dest='command')
    
    # web-fetch
    p = sub.add_parser('web-fetch', help='Fetch and extract text from URL')
    p.add_argument('url', help='URL to fetch')
    p.add_argument('-o', '--output', help='Save to file')
    
    # json-query  
    p = sub.add_parser('json-query', help='Query JSON with dot notation')
    p.add_argument('file', help='JSON file')
    p.add_argument('query', help='Dot-notation path (e.g., users.0.name)')
    
    # file-watch
    p = sub.add_parser('file-watch', help='Watch directory and run command on changes')
    p.add_argument('directory', help='Directory to watch')
    p.add_argument('command', help='Command to run')
    p.add_argument('-p', '--pattern', default='*', help='File pattern (default: *)')
    p.add_argument('-i', '--interval', type=int, default=5, help='Check interval in seconds')
    
    args = parser.parse_args()
    
    if args.command == 'web-fetch':
        return web_fetch(args.url, args.output)
    elif args.command == 'json-query':
        return json_query(args.file, args.query)
    elif args.command == 'file-watch':
        return file_watch(args.directory, args.command, args.pattern, args.interval)
    else:
        parser.print_help()
        return 1

if __name__ == '__main__':
    sys.exit(main())
