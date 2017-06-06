import scraper

def main():

    ws = scraper.WebScraper('https://en.wikipedia.org/wiki/Lebron_James')
    ws.scrape()

main()
