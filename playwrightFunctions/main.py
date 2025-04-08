import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()
        
        await page.goto("https://qp-genie.azurewebsites.net/")
        
        await page.fill('input[name="username"]', "admin@synergech.com")
        await page.fill('input[name="password"]', "admin")
        
        await page.click('button[type="submit"]')
        
        await page.wait_for_timeout(3000)  # simulate wait
        content = await page.content()
        
        if "Dashboard" in content or "Genie AI" in content:
            print("Login successful.")
        else:
            print("Login failed or still on login page.")

        await browser.close()

# Run the script
asyncio.run(run())