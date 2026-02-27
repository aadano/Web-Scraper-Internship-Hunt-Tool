import sqlite3
from playwright.sync_api import sync_playwright

def scrape_devpost():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://devpost.com/hackathons")
        page.wait_for_selector("div.hackathon-tile")

        hackathons = page.query_selector_all("div.hackathon-tile")

        conn = sqlite3.connect("events.db")
        cursor = conn.cursor()

        for hackathon in hackathons:
            name = hackathon.query_selector("h3").inner_text().strip()
            link = hackathon.query_selector("a").get_attribute("href")

            date_el = hackathon.query_selector("div.submission-period")
            date = date_el.inner_text().strip() if date_el else "N/A"

            try: 
                cursor.execute("""
                    INSERT INTO events (name, type, date, link, source)
                    VALUES (?, ?, ?, ?, ?)
                """, (name, "hackathon", date, link, "devpost"))
            except sqlite3.IntegrityError:
                pass

        conn.commit()
        conn.close()
        browser.close()
        print("Done scraping Devpost!")

if __name__ == "__main__":
    scrape_devpost()