"""Confirm nav theme/lang preservation works in BOTH starting themes."""
import asyncio
from playwright.async_api import async_playwright

BASE = "http://127.0.0.1:8910"


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()

        # Start in DARK + ES — check toggle icon, theme toggle href, lang EN href
        ctx = await browser.new_context(viewport={"width": 1280, "height": 800})
        page = await ctx.new_page()
        await page.goto(f"{BASE}/?page=home&lang=es&theme=dark", wait_until="domcontentloaded")
        await page.wait_for_timeout(400)
        toggle_text = await page.evaluate("document.querySelector('.theme-tgl').textContent")
        toggle_href = await page.evaluate("document.querySelector('.theme-tgl').getAttribute('href')")
        en_href = await page.evaluate("Array.from(document.querySelectorAll('.lang-switch a')).find(a=>a.textContent.trim()==='EN').getAttribute('href')")
        ghk_href = await page.evaluate("Array.from(document.querySelectorAll('.nav-links a')).find(a=>a.textContent.trim().toUpperCase()==='GHK-CU').getAttribute('href')")
        await page.screenshot(path="/tmp/pauli-darkmode-nav.png", clip={"x":0,"y":0,"width":1280,"height":80})
        print(f"DARK home-es: toggle_icon={toggle_text!r}  toggle_href={toggle_href!r}")
        print(f"            EN_href={en_href!r}")
        print(f"            GHK_href={ghk_href!r}")
        assert toggle_text.strip() == "🌙", f"Expected 🌙 in dark, got {toggle_text!r}"
        assert "theme=light" in toggle_href, f"Expected theme=light in toggle href, got {toggle_href!r}"
        assert "theme=dark" in en_href, f"Lang switch should preserve dark theme, got {en_href!r}"
        assert "theme=dark" in ghk_href, f"GHK link should preserve dark theme, got {ghk_href!r}"
        print("PASS: dark mode nav links all preserve theme=dark and toggle flips to light")
        await ctx.close()

        # Start in LIGHT + EN
        ctx = await browser.new_context(viewport={"width": 1280, "height": 800})
        page = await ctx.new_page()
        await page.goto(f"{BASE}/?page=ghk&lang=en&theme=light", wait_until="domcontentloaded")
        await page.wait_for_timeout(400)
        toggle_text = await page.evaluate("document.querySelector('.theme-tgl').textContent")
        toggle_href = await page.evaluate("document.querySelector('.theme-tgl').getAttribute('href')")
        es_href = await page.evaluate("Array.from(document.querySelectorAll('.lang-switch a')).find(a=>a.textContent.trim()==='ES').getAttribute('href')")
        print(f"LIGHT ghk-en: toggle_icon={toggle_text!r}  toggle_href={toggle_href!r}")
        print(f"             ES_href={es_href!r}")
        assert toggle_text.strip() == "☀️", f"Expected ☀️ in light, got {toggle_text!r}"
        assert "theme=dark" in toggle_href, f"Expected theme=dark in toggle href, got {toggle_href!r}"
        assert "theme=light" in es_href, f"Lang switch should preserve light theme, got {es_href!r}"
        print("PASS: light mode nav links all preserve theme=light and toggle flips to dark")
        await ctx.close()

        await browser.close()
        print()
        print("ALL THEME PRESERVATION CHECKS PASSED")


asyncio.run(main())
