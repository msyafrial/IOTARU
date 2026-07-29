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
        
        # -> Click the 'Products' link in the top navigation to open the Products page.
        # Products link
        elem = page.get_by_text('Contact Us', exact=True).locator("xpath=ancestor-or-self::*[.//a][1]").get_by_role('link', name='Products', exact=True)
        await elem.click(timeout=10000)
        
        # -> Scroll down until the product grid is visible, then click the 'IOTARU Smart Meter' product card to open its detail page.
        await page.mouse.wheel(0, 300)
        
        # -> Scroll down until the product grid is visible, then click the 'IOTARU Smart Meter' product card to open its detail page.
        # Monitoring IOTARU Smart Meter Precision energy... link
        elem = page.locator('a[href="/products/smart-meter"]')
        await elem.click(timeout=10000)
        
        # -> Scroll down and verify the product detail page shows the visible headings 'Specifications' and 'Features'.
        await page.mouse.wheel(0, 300)
        
        # --> Assertions to verify final state
        
        # --> Verify product specifications and features are displayed
        # Assert: The specifications/features table header 'Feature' and 'Detail' is visible.
        await expect(page.locator("xpath=/html/body/main/section[2]/div/div/div[2]/div/div/table/thead/tr").nth(0)).to_have_text("Feature\nDetail", timeout=15000), "The specifications/features table header 'Feature' and 'Detail' is visible."
        # Assert: The 'Circuits' specification showing 'Up to 32 channels' is displayed.
        await expect(page.locator("xpath=/html/body/main/section[2]/div/div/div[2]/div/div/table/tbody/tr[1]").nth(0)).to_have_text("Circuits\nUp to 32 channels", timeout=15000), "The 'Circuits' specification showing 'Up to 32 channels' is displayed."
        # Assert: The 'Accuracy' specification showing '±0.5%' is displayed.
        await expect(page.locator("xpath=/html/body/main/section[2]/div/div/div[2]/div/div/table/tbody/tr[2]").nth(0)).to_have_text("Accuracy\n\u00b10.5%", timeout=15000), "The 'Accuracy' specification showing '\u00b10.5%' is displayed."
        # Assert: The 'Sampling Rate' specification showing '1kHz' is displayed.
        await expect(page.locator("xpath=/html/body/main/section[2]/div/div/div[2]/div/div/table/tbody/tr[3]").nth(0)).to_have_text("Sampling Rate\n1kHz", timeout=15000), "The 'Sampling Rate' specification showing '1kHz' is displayed."
        # Assert: The 'Connectivity' specification showing 'Ethernet / Modbus TCP' is displayed.
        await expect(page.locator("xpath=/html/body/main/section[2]/div/div/div[2]/div/div/table/tbody/tr[4]").nth(0)).to_have_text("Connectivity\nEthernet / Modbus TCP", timeout=15000), "The 'Connectivity' specification showing 'Ethernet / Modbus TCP' is displayed."
        # Assert: The 'Display' specification showing '7“ touchscreen' is displayed.
        await expect(page.locator("xpath=/html/body/main/section[2]/div/div/div[2]/div/div/table/tbody/tr[5]").nth(0)).to_have_text("Display\n7\u201c touchscreen", timeout=15000), "The 'Display' specification showing '7\u201c touchscreen' is displayed."
        await asyncio.sleep(5)

    finally:
        if context:
            await context.close()
        if browser:
            await browser.close()
        if pw:
            await pw.stop()

asyncio.run(run_test())
    