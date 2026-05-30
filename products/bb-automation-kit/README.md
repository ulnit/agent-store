# 🎯 Bug Bounty Automation Kit

**Zero-dependency recon toolkit for security researchers.** Subdomain discovery, live probing, vuln scanning — all in pure Python.

## Quick Start
```bash
pip install bb-automation-kit
# or
git clone https://github.com/ulnit/bb-automation-kit
```

## Commands

```bash
# Discover subdomains
python3 bb_kit.py enum tesla.com

# Probe live hosts  
python3 bb_kit.py probe api.tesla.com www.tesla.com app.tesla.com

# Quick vulnerability scan
python3 bb_kit.py scan https://example.com
```

## Why This Over Alternatives?

| Tool | Deps | Language | This |
|------|------|----------|------|
| subfinder | Go toolchain | Go | Python (stdlib) |
| amass | Go + binaries | Go | Python (stdlib) |
| httpx | Go toolchain | Go | Python (stdlib) |

**Zero external dependencies.** Runs on any system with Python 3.8+.

## Pricing
**Free**: 100 domains/day  
**Pro ($15)**: Unlimited + concurrent scanning + priority support

[Buy Pro — $15](https://paypal.me/ulnit/15)
