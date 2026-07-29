import asyncio
import re
from playwright import async_api
from playwright.async_api import expect

async def run_test():
    pw = None
    browser = None
    context = None

    try:
        # Start a Playwright session in asynchronous mode
        pw = await async_api.async_playwright().start()

        # Launch a Chromium browser in headless mode with custom arguments
        browser = await pw.chromium.launch(
            headless=True,
            args=[
                "--window-size=1280,720",
                "--disable-dev-shm-usage",
                "--ipc=host",
                "--single-process"
            ],
        )

        # Create a new browser context (like an incognito window)
        context = await browser.new_context()
        # Wider default timeout to match the agent's DOM-stability budget;
        # auto-waiting Playwright APIs (expect, locator.wait_for) inherit this.
        context.set_default_timeout(15000)

        # Open a new page in the browser context
        page = await context.new_page()

        # Interact with the page elements to simulate user flow
        # -> navigate
        await page.goto("http://localhost:4321/solutions")
        try:
            await page.wait_for_load_state("domcontentloaded", timeout=5000)
        except Exception:
            pass
        
        # -> Open the 'Blog' page by clicking the 'Blog' link in the header.
        # Blog link
        elem = page.get_by_text('Contact Us', exact=True).locator("xpath=ancestor-or-self::*[.//a][1]").get_by_role('link', name='Blog', exact=True)
        await elem.click(timeout=10000)
        
        # -> Scroll down to the article list on the 'Our Blog' page to reveal blog post cards.
        await page.mouse.wheel(0, 300)
        
        # -> Click the 'Getting Started with IoT: A Beginner's Guide' blog post card to open its article detail page.
        # July 20, 2026 Getting Started with IoT: A... link
        elem = page.locator('a[href="/blog/getting-started-iot"]')
        await elem.click(timeout=10000)
        
        # -> Scroll the 'Getting Started with IoT: A Beginner's Guide' article page and look for post body text to verify the full article content is displayed.
        await page.mouse.wheel(0, 300)
        
        # -> Scroll the article page down to reveal the 'Conclusion' paragraph and the 'Related Posts' section and verify the full article content is visible.
        await page.mouse.wheel(0, 300)
        
        # --> Assertions to verify final state
        
        # --> Verify the selected article page is displayed
        # Assert: The URL contains '/blog/getting-started-iot', confirming the selected article page is displayed.
        await expect(page).to_have_url(re.compile("/blog/getting\\-started\\-iot"), timeout=15000), "The URL contains '/blog/getting-started-iot', confirming the selected article page is displayed."
        
        # --> Verify the full article content is displayed
        # Assert: The browser is on the article detail URL for the selected post.
        await expect(page).to_have_url(re.compile("blog/getting\\-started\\-iot"), timeout=15000), "The browser is on the article detail URL for the selected post."
        await page.locator("xpath=/html/body/main/section[2]/div/div[3]/div[1]/a").nth(0).scroll_into_view_if_needed()
        # Assert: The 'IoT Security Best Practices' related post link is visible on the article page.
        await expect(page.locator("xpath=/html/body/main/section[2]/div/div[3]/div[1]/a").nth(0)).to_be_visible(timeout=15000), "The 'IoT Security Best Practices' related post link is visible on the article page."
        await page.locator("xpath=/html/body/main/section[2]/div/div[3]/div[2]/a").nth(0).scroll_into_view_if_needed()
        # Assert: The 'Smart Home Automation: Complete Guide' related post link is visible on the article page.
        await expect(page.locator("xpath=/html/body/main/section[2]/div/div[3]/div[2]/a").nth(0)).to_be_visible(timeout=15000), "The 'Smart Home Automation: Complete Guide' related post link is visible on the article page."
        await asyncio.sleep(5)

    finally:
        if context:
            await context.close()
        if browser:
            await browser.close()
        if pw:
            await pw.stop()

asyncio.run(run_test())
    