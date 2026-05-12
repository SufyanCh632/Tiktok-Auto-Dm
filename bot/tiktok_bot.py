import time
import random
from playwright.sync_api import sync_playwright

AUTO_REPLIES = {
    'price': 'Our pricing starts from $99 😊',
    'service': 'We help creators grow their audience 🚀',
    'hello': 'Hey 👋 Nice to hear from you!'
}

def delay(min_sec=2, max_sec=5):
    time.sleep(random.uniform(min_sec, max_sec))

def send_bulk_dms(usernames, message):

    try:

        with sync_playwright() as p:

            browser = p.chromium.launch(
                headless=False
            )

            context = browser.new_context(
                storage_state='session.json'
            )

            page = context.new_page()

            for username in usernames:

                username = username.strip()

                if not username:
                    continue

                try:

                    page.goto(
                        f'https://www.tiktok.com/@{username}'
                    )

                    delay()

                    page.click(
                        'button:has-text("Message")'
                    )

                    delay()

                    page.fill(
                        'div[contenteditable="true"]',
                        message
                    )

                    delay()

                    page.keyboard.press('Enter')

                    print(
                        f'Message sent to {username}'
                    )

                    delay(4, 8)

                except Exception as e:
                    print(
                        f'Failed for {username}: {e}'
                    )

            browser.close()

        return 'DMs sent Successfully'

    except Exception as e:
        return str(e)
