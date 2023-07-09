# Web scraping demo
Demo for scraping using scrapy, parsing a real website and extracting key information. In this case we query [Scrapethissite](http://www.scrapethissite.com/pages/forms/) that has database of NHL stats since 1990.
We extract the data and save it to a csv file. Data in this case consists of team name, year, wins and losses.

Install Scrapy in a virtual environment:

```bash
$ python3 -m venv venv
$ source venv/Scripts/activate
$ pip install scrapy
```

Run the spider:

```bash
$ cd hockey
$ scrapy crawl stats
```
