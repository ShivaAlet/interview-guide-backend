from flask import Flask, request, jsonify
import asyncio
from pyppeteer import launch
import nest_asyncio

nest_asyncio.apply()
app = Flask(__name__)

@app.route('/search')
def search():
    query = request.args.get('q')
    if not query:
        return jsonify({"error": "Query required"}), 400

    results = asyncio.get_event_loop().run_until_complete(scrape_google(query))
    return jsonify(results)

async def scrape_google(query):
    browser = await launch(headless=True)
    page = await browser.newPage()
    await page.goto(f'https://www.google.com/search?q={query}')
    await page.waitForSelector('h3')

    elements = await page.querySelectorAll('div.tF2Cxc')
    results = []

    for el in elements:
        title_el = await el.querySelector('h3')
        link_el = await el.querySelector('a')
        if title_el and link_el:
            title = await page.evaluate('(element) => element.innerText', title_el)
            link = await page.evaluate('(element) => element.href', link_el)
            results.append({"title": title, "link": link})

    await browser.close()
    return results

if __name__ == '__main__':
    app.run(debug=True)
