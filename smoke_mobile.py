"""Mobile + dark theme + responsive smoke."""
import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

BASE = "http://127.0.0.1:8910"


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()

        # Desktop dark
        ctx = await browser.new_context(viewport={"width": 1280, "height": 800})
        page = await ctx.new_page()
        await page.goto(f"{BASE}/?page=home&lang=es&theme=dark", wait_until="domcontentloaded")
        await page.wait_for_timeout(500)
        nav_bg = await page.evaluate("getComputedStyle(document.querySelector('.topnav')).backgroundColor")
        body_bg = await page.evaluate("getComputedStyle(document.body).backgroundColor")
        await page.screenshot(path="/tmp/pauli-home-es-dark-desktop.png")
        print(f"DESKTOP DARK home-es: nav-bg={nav_bg}  body-bg={body_bg}")
        await ctx.close()

        # Mobile light home
        ctx = await browser.new_context(viewport={"width": 375, "height": 812}, device_scale_factor=2)
        page = await ctx.new_page()
        await page.goto(f"{BASE}/?page=home&lang=es&theme=light", wait_until="domcontentloaded")
        await page.wait_for_timeout(500)
        nav_links_visible = await page.evaluate(
            "getComputedStyle(document.querySelector('.nav-links')).display"
        )
        await page.screenshot(path="/tmp/pauli-home-es-light-mobile.png")
        print(f"MOBILE LIGHT home-es: .nav-links display={nav_links_visible} (should be 'none' below 900px)")
        await ctx.close()

        # Mobile dark estudios
        ctx = await browser.new_context(viewport={"width": 375, "height": 812}, device_scale_factor=2)
        page = await ctx.new_page()
        await page.goto(f"{BASE}/?page=estudios&lang=es&theme=dark", wait_until="domcontentloaded")
        await page.wait_for_timeout(500)
        await page.screenshot(path="/tmp/pauli-estudios-es-dark-mobile.png")
        print("MOBILE DARK estudios-es: screenshot saved")
        await ctx.close()

        # Theme toggle round-trip (start light, click theme toggle, confirm goes dark)
        ctx = await browser.new_context(viewport={"width": 1280, "height": 800})
        page = await ctx.new_page()
        await page.goto(f"{BASE}/?page=home&lang=es&theme=light", wait_until="domcontentloaded")
        await page.wait_for_timeout(300)
        toggle_href = await page.evaluate("document.querySelector('.theme-tgl').getAttribute('href')")
        print(f"theme toggle href on light page: {toggle_href}")
        # navigate by href
        await page.goto(BASE + "/" + toggle_href, wait_until="domcontentloaded")
        await page.wait_for_timeout(300)
        is_dark = await page.evaluate("document.documentElement.classList.contains('theme-dark')")
        print(f"after clicking toggle, html.theme-dark = {is_dark} (expected True)")
        await ctx.close()

        # Lang switch round-trip
        ctx = await browser.new_context(viewport={"width": 1280, "height": 800})
        page = await ctx.new_page()
        await page.goto(f"{BASE}/?page=home&lang=es&theme=light", wait_until="domcontentloaded")
        await page.wait_for_timeout(300)
        en_href = await page.evaluate("Array.from(document.querySelectorAll('.lang-switch a')).find(a=>a.textContent.trim()==='EN').getAttribute('href')")
        print(f"EN switch href: {en_href}")
        await page.goto(BASE + "/" + en_href, wait_until="domcontentloaded")
        await page.wait_for_timeout(500)
        hero_text = await page.inner_text(".hero-top")
        print(f"after EN switch, hero starts with: {hero_text[:60]!r}")
        await ctx.close()

        await browser.close()


asyncio.run(main())
