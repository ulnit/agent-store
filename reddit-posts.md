# Reddit — Copy-Paste Posts

## r/SideProject — "I built an AI Video Factory on a $35 Raspberry Pi"

**Title:** I built an AI Video Factory on a $35 Raspberry Pi — it makes videos while I sleep

**Body:**

I wanted a YouTube channel. I hated editing videos. So I automated the entire thing.

[AI Video Factory](https://github.com/ulnit/ai-video-factory) does this every morning at 7 AM:

1. Researches trending AI topics
2. Writes a script
3. Generates 1080p slides with gradients, typography, and icons
4. Adds background music
5. Assembles everything into a finished video

Zero human clicks. Zero cloud costs. Running on a $35 Raspberry Pi with Python, Pillow, and FFmpeg.

I've been building AI products this way for 6 months. Now at 23 products on the same Pi. My monthly infrastructure cost: $0.

Happy to answer any questions about the stack, automation, or building on a Pi.

Edit: Wow, thanks for the support! For those asking — yes, the entire code is open source. [Here's the repo](https://github.com/ulnit/ai-video-factory).

---

## r/Python — "How I built a video rendering pipeline with pure Python stdlib"

**Title:** I built a video rendering pipeline using only Python stdlib + Pillow + FFmpeg

**Body:**

No FastAPI. No Django. No numpy. Just stdlib.

The pipeline:
```python
# Topic research → Script writing → Slide generation → Video assembly
# All orchestrated by a single Python file + cron
```

**Slide generation** uses Pillow with gradient backgrounds, auto-wrapped text, and emoji icons. Each slide is 1080p.

**Video assembly** uses FFmpeg via subprocess to concatenate slides with background music and transitions.

**Scheduling** is just cron. No Celery, no Airflow. `0 7 * * * python3 engine.py`

The entire thing runs on a $35 Raspberry Pi. I'm not kidding.

[Source code](https://github.com/ulnit/ai-video-factory) is open source. Stars appreciated ⭐

---

## r/SaaS — "My SaaS has $0 monthly infrastructure cost. Here's how."

**Title:** My SaaS stack costs $0/month to run (23 products on a $35 Pi)

**Body:**

I see posts about $500/mo AWS bills before making a dollar. Here's the opposite approach.

**My stack:**
- Hardware: $35 Raspberry Pi (one-time)
- Runtime: Python 3 stdlib
- Hosting: GitHub Pages (free)
- Scheduling: Cron (built into Linux)
- Payments: PayPal (no monthly fee)

**23 products running 24/7:**
- AI Video Factory ($9/mo subscription model)
- AI Trading Signals ($29-99/mo)
- AI API Gateway ($9/mo)

Total monthly infra cost: $0. Every sale is pure profit.

The key insight: If your product can run on a Pi, you don't need the cloud. Python stdlib + cron + GitHub Pages handles 95% of SaaS needs.

I'm happy to help anyone trying to reduce their infrastructure costs. AMA.