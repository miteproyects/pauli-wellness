"""Playwright smoke test for the static Pauli site served at :8910.

Visits each (page, lang, theme) combination, captures:
- Console errors / warnings
- Whether key content rendered (nav, hero, footer)
- A screenshot to /tmp/pauli-{page}-{lang}-{theme}.png
"""
import asyncio
import sys
from pathlib import Path
from playwright.async_api import async_playwright

BASE = "http://127.0.0.1:8910"

COMBOS = [
    # (page, lang, theme, expected_text_snippet)
    ("home", "es", "light", "Dos décadas de ciencia"),
    ("home", "es", "dark",  "Dos décadas de ciencia"),
    ("home", "en", "light", "Two decades of science"),
    ("ghk", "es", "light",  "GHK-Cu · el péptido"),
    ("ghk", "en", "light",  "GHK-Cu · the peptide"),
    ("resultados", "es", "light", "Resultados que cuentan"),
    ("resultados", "en", "light", "Results people share"),
    ("estudios", "es", "light", "Estudios y patentes"),
    ("estudios", "en", "light", "Studies and patents"),
]

OUT_DIR = Path("/tmp")


async def main():
    failures = []
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        for (page_id, lang, theme, expected) in COMBOS:
            ctx = await browser.new_context(viewport={"width": 1280, "height": 800})
            page = await ctx.new_page()
            console_msgs = []
            page.on("console", lambda m: console_msgs.append(f"{m.type}: {m.text}"))
            page.on("pageerror", lambda e: console_msgs.append(f"PAGEERROR: {e}"))

            url = f"{BASE}/?page={page_id}&lang={lang}&theme={theme}"
            try:
                resp = await page.goto(url, wait_until="domcontentloaded", timeout=10000)
                await page.wait_for_timeout(500)  # let router JS run
                status = resp.status if resp else 0
                body_text = await page.inner_text("body")
                nav_present = await page.locator(".topnav").count() > 0
                hero_present = await page.locator(".hero-top, .page-hero h1").count() > 0
                footer_present = await page.locator(".footer").count() > 0
                wa_fab_present = await page.locator(".wa-float").count() > 0
                main_html_len = len(await page.locator("#main").inner_html())
                expected_ok = expected in body_text

                errs = [m for m in console_msgs if m.startswith(("error:", "PAGEERROR:"))]
                warns = [m for m in console_msgs if m.startswith("warning:")]

                screenshot_path = OUT_DIR / f"pauli-{page_id}-{lang}-{theme}.png"
                await page.screenshot(path=str(screenshot_path), full_page=False)

                row = f"{page_id:>10s} {lang} {theme:>5s}  status={status}  nav={nav_present} hero={hero_present} footer={footer_present} wa={wa_fab_present} main_len={main_html_len:>6d}  expected_ok={expected_ok}  errs={len(errs)} warns={len(warns)}  ⇒ {screenshot_path.name}"
                print(row)
                if errs:
                    for e in errs[:5]:
                        print(f"   ⚠ {e[:160]}")
                if not (nav_present and hero_present and footer_present and wa_fab_present and expected_ok):
                    failures.append(row)
            except Exception as e:
                print(f"{page_id} {lang} {theme} ✗ EXCEPTION: {e}")
                failures.append(f"{page_id} {lang} {theme}: {e}")
            await ctx.close()
        await browser.close()

    print()
    if failures:
        print(f"[smoke] FAILURES: {len(failures)}")
        for f in failures:
            print(f"  {f}")
        sys.exit(1)
    else:
        print(f"[smoke] all {len(COMBOS)} combos PASSED")


asyncio.run(main())
