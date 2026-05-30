# 🛠️ AI Agent Toolkit

**Production-ready CLI tools for AI agent developers.** Zero dependencies. Python stdlib only.

## Quick Install
```bash
curl -sSL https://raw.githubusercontent.com/ulnit/ai-agent-toolkit/main/install.sh | bash
```

Or:
```bash
pip install ai-agent-toolkit
```

## Tools

### 🌐 `web-fetch` — Extract clean text from any URL
```bash
agent-tools web-fetch "https://example.com"
agent-tools web-fetch "https://blog.example.com" -o article.txt
```
Strips HTML, scripts, styles. Leaves clean readable text. Perfect for AI ingestion.

### 📋 `json-query` — Query JSON with simple dot notation
```bash
agent-tools json-query data.json "users.0.name"
agent-tools json-query api-response.json "data.items.0.title"
```
No more writing jq expressions. Just dots.

### 👁️ `file-watch` — React to file changes automatically
```bash
agent-tools file-watch ./src "make build" -p "*.py" -i 3
```
Great for auto-reloading dev servers, triggering AI pipelines on new data.

## Why This Toolkit?

| Feature | This Toolkit | Alternatives |
|---------|-------------|-------------|
| Dependencies | **Zero** (stdlib only) | jq (C), pup (Go), entr (C) |
| Cross-platform | ✅ Linux/Mac/Windows | Varies |
| AI-friendly output | ✅ Clean text, structured JSON | Raw HTML/XML |
| Pipeable | ✅ stdin/stdout | Limited |
| Size | **< 200 lines** | 1000s of lines |

## Pricing

**Free tier**: 100 requests/day  
**Pro tier**: $9 one-time — unlimited usage + priority support  
**Team tier**: $29 — commercial use + custom integrations

[Buy Pro - $9](https://www.paypal.com/instantcommerce/checkout/EXAMPLE) | [Buy Team - $29](https://www.paypal.com/instantcommerce/checkout/EXAMPLE)

---

Built with ❤️ for the AI agent community. MIT License.
