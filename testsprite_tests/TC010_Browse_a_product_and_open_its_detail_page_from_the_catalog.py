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
        
        # -> Click the 'IOTARU Smart Gateway' product card to open its detail page.
        # Gateway IOTARU Smart Gateway Central hub that... link
        elem = page.locator('a[href="/products/smart-gateway"]')
        await elem.click(timeout=10000)
        
        # -> Scroll down the product detail page and locate the 'Specifications' or 'Features' section on the IOTARU Smart Gateway page.
        await page.mouse.wheel(0, 300)
        
        # --> Assertions to verify final state
        
        # --> Verify the selected product detail page is displayed
        # Assert: The URL contains /products/smart-gateway, confirming the product detail page is open.
        await expect(page).to_have_url(re.compile("/products/smart\\-gateway"), timeout=15000), "The URL contains /products/smart-gateway, confirming the product detail page is open."
        # Assert: The Specifications table shows the expected 'Protocols' value for the selected product.
        await expect(page.locator("xpath=/html/body/main/section[2]/div/div/div[2]/div/div/table/tbody/tr[1]/td[2]").nth(0)).to_have_text("Zigbee 3.0, Z-Wave, Wi-Fi 6, BLE 5.0", timeout=15000), "The Specifications table shows the expected 'Protocols' value for the selected product."
        
        # --> Verify product specifications and features are displayed
        # Assert: The specifications table header 'Feature / Detail' is visible.
        await expect(page.locator("xpath=/html/body/main/section[2]/div/div/div[2]/div/div/table/thead/tr").nth(0)).to_have_text("Feature\nDetail", timeout=15000), "The specifications table header 'Feature / Detail' is visible."
        # Assert: The 'Protocols' specification shows the expected protocols.
        await expect(page.locator("xpath=/html/body/main/section[2]/div/div/div[2]/div/div/table/tbody/tr[1]/td[2]").nth(0)).to_have_text("Zigbee 3.0, Z-Wave, Wi-Fi 6, BLE 5.0", timeout=15000), "The 'Protocols' specification shows the expected protocols."
        # Assert: The 'Processor' specification shows the expected processor.
        await expect(page.locator("xpath=/html/body/main/section[2]/div/div/div[2]/div/div/table/tbody/tr[2]/td[2]").nth(0)).to_have_text("Quad-core ARM Cortex-A53", timeout=15000), "The 'Processor' specification shows the expected processor."
        # Assert: The 'Memory' specification shows the expected memory and storage.
        await expect(page.locator("xpath=/html/body/main/section[2]/div/div/div[2]/div/div/table/tbody/tr[3]/td[2]").nth(0)).to_have_text("2GB RAM / 16GB Storage", timeout=15000), "The 'Memory' specification shows the expected memory and storage."
        # Assert: The 'Ethernet' specification shows the expected ethernet capability.
        await expect(page.locator("xpath=/html/body/main/section[2]/div/div/div[2]/div/div/table/tbody/tr[4]/td[2]").nth(0)).to_have_text("Gigabit Ethernet", timeout=15000), "The 'Ethernet' specification shows the expected ethernet capability."
        # Assert: The 'Power' specification shows the expected power options.
        await expect(page.locator("xpath=/html/body/main/section[2]/div/div/div[2]/div/div/table/tbody/tr[5]/td[2]").nth(0)).to_have_text("USB-C / Battery Backup", timeout=15000), "The 'Power' specification shows the expected power options."
        await asyncio.sleep(5)

    finally:
        if context:
            await context.close()
        if browser:
            await browser.close()
        if pw:
            await pw.stop()

asyncio.run(run_test())
    