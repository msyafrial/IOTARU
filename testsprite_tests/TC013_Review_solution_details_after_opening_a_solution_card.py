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
        
        # -> Scroll down the 'IoT Solutions' page to reveal the solutions grid and locate solution cards.
        await page.mouse.wheel(0, 300)
        
        # -> Click the 'Smart Home' solution card from the solutions grid to open its detail page.
        # Smart Home Complete IoT ecosystem for modern... link
        elem = page.locator('a[href="/solutions/smart-home"]')
        await elem.click(timeout=10000)
        
        # --> Assertions to verify final state
        
        # --> Verify solution benefits are displayed
        # Assert: The 'Unified Control' benefit is displayed.
        await expect(page.locator("xpath=/html/body/main/section[2]/div/div[1]/div/div/table/tbody/tr[1]/td[1]").nth(0)).to_have_text("Unified Control", timeout=15000), "The 'Unified Control' benefit is displayed."
        # Assert: The 'Energy Savings' benefit is displayed.
        await expect(page.locator("xpath=/html/body/main/section[2]/div/div[1]/div/div/table/tbody/tr[2]/td[1]").nth(0)).to_have_text("Energy Savings", timeout=15000), "The 'Energy Savings' benefit is displayed."
        # Assert: The 'Security First' benefit is displayed.
        await expect(page.locator("xpath=/html/body/main/section[2]/div/div[1]/div/div/table/tbody/tr[3]/td[1]").nth(0)).to_have_text("Security First", timeout=15000), "The 'Security First' benefit is displayed."
        # Assert: The 'Voice Ready' benefit is displayed.
        await expect(page.locator("xpath=/html/body/main/section[2]/div/div[1]/div/div/table/tbody/tr[4]/td[1]").nth(0)).to_have_text("Voice Ready", timeout=15000), "The 'Voice Ready' benefit is displayed."
        # Assert: The 'Offline Capable' benefit is displayed.
        await expect(page.locator("xpath=/html/body/main/section[2]/div/div[1]/div/div/table/tbody/tr[5]/td[1]").nth(0)).to_have_text("Offline Capable", timeout=15000), "The 'Offline Capable' benefit is displayed."
        current_url = await page.evaluate("() => window.location.href")
        # Assert: page loaded with a URL (final outcome verified by the AI judge during the run)
        assert current_url, 'Page should have loaded with a URL'
        await asyncio.sleep(5)

    finally:
        if context:
            await context.close()
        if browser:
            await browser.close()
        if pw:
            await pw.stop()

asyncio.run(run_test())
    