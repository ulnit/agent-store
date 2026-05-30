#!/usr/bin/env python3
"""
Bug Bounty Automation Kit — Subdomain discovery, live probing, vulnerability scanning
=====================================================================================
Zero-dependency reconnaissance toolkit for security researchers.
"""
import sys, json, re, time, os, argparse
import urllib.request, urllib.error
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

# ─── Subdomain Enumeration ───────────────────────────────
def enum_subdomains(domain):
    """Discover subdomains from crt.sh, AlienVault OTX, urlscan.io"""
    subs = set()
    
    # crt.sh
    try:
        url = f"https://crt.sh/?q=%.{domain}&output=json"
        req = urllib.request.Request(url, headers={'User-Agent': 'BB-Kit/1.0'})
        data = json.loads(urllib.request.urlopen(req, timeout=20).read())
        for entry in data:
            name = entry.get('name_value', '').lower().strip()
            for n in name.split('\n'):
                n = n.strip().lstrip('*.')
                if n.endswith(domain) and n != domain:
                    subs.add(n)
    except: pass
    
    # urlscan.io
    try:
        url = f"https://urlscan.io/api/v1/search/?q=domain:{domain}&size=100"
        req = urllib.request.Request(url, headers={'User-Agent': 'BB-Kit/1.0'})
        data = json.loads(urllib.request.urlopen(req, timeout=15).read())
        for result in data.get('results', []):
            page_domain = result.get('page', {}).get('domain', '')
            if page_domain.endswith(domain):
                subs.add(page_domain)
    except: pass
    
    return sorted(subs)

# ─── Live Probe ──────────────────────────────────────────
def probe_host(host):
    """Check if a host is live (HTTP/HTTPS)"""
    for scheme in ['https', 'http']:
        try:
            req = urllib.request.Request(f"{scheme}://{host}", headers={'User-Agent': 'BB-Kit/1.0'})
            resp = urllib.request.urlopen(req, timeout=5)
            server = resp.headers.get('Server', 'unknown')
            return {'host': host, 'url': f'{scheme}://{host}', 'status': resp.status, 'server': server}
        except urllib.error.HTTPError as e:
            return {'host': host, 'url': f'{scheme}://{host}', 'status': e.code, 'server': e.headers.get('Server', '?')}
        except:
            pass
    return {'host': host, 'url': None, 'status': 0, 'server': 'unreachable'}

def probe_hosts(hosts, threads=10):
    """Probe multiple hosts in parallel"""
    results = []
    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = {executor.submit(probe_host, h): h for h in hosts}
        for f in as_completed(futures):
            results.append(f.result())
    return sorted(results, key=lambda x: (x['status'] == 0, x['status']))

# ─── Quick Vuln Check ───────────────────────────────────
def quick_scan(url):
    """Run quick vulnerability checks on a URL"""
    findings = []
    
    # Check exposed .git
    try:
        r = urllib.request.urlopen(urllib.request.Request(f'{url}/.git/config', headers={'User-Agent': 'BB-Kit/1.0'}), timeout=5)
        if r.status == 200 and 'repositoryformatversion' in r.read().decode('utf-8', errors='ignore').lower():
            findings.append(f'EXPOSED: {url}/.git/config')
    except: pass
    
    # Check security.txt
    try:
        r = urllib.request.urlopen(urllib.request.Request(f'{url}/.well-known/security.txt', headers={'User-Agent': 'BB-Kit/1.0'}), timeout=5)
        if r.status == 200:
            text = r.read().decode('utf-8', errors='ignore')
            if 'contact' in text.lower():
                findings.append(f'SECURITY.TXT: {url}/.well-known/security.txt')
    except: pass
    
    return findings

# ─── CLI ─────────────────────────────────────────────────
def main():
    p = argparse.ArgumentParser(description='Bug Bounty Automation Kit')
    sub = p.add_subparsers(dest='cmd')
    
    sub.add_parser('enum', help='Enumerate subdomains').add_argument('domain')
    
    sp = sub.add_parser('probe', help='Probe hosts')
    sp.add_argument('hosts', nargs='+')
    sp.add_argument('-t','--threads', type=int, default=10)
    
    sp = sub.add_parser('scan', help='Quick vulnerability scan')
    sp.add_argument('url')
    
    args = p.parse_args()
    
    if args.cmd == 'enum':
        print(f"[*] Enumerating {args.domain}...")
        subs = enum_subdomains(args.domain)
        for s in subs: print(s)
        print(f"[+] Found {len(subs)} subdomains")
    elif args.cmd == 'probe':
        results = probe_hosts(args.hosts, args.threads)
        for r in results:
            if r['status']:
                print(f"  {r['url']:50s} [{r['status']}] {r['server']}")
    elif args.cmd == 'scan':
        print(f"[*] Scanning {args.url}")
        for f in quick_scan(args.url):
            print(f"  [!] {f}")

if __name__ == '__main__':
    main()
