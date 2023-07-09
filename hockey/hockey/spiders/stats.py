import scrapy
import csv


class StatsSpider(scrapy.Spider):
    name = "stats"
    allowed_domains = ["scrapethissite.com"]
    start_urls = ["http://www.scrapethissite.com/pages/forms/"]

    def parse(self, response):
        table = response.xpath('//table')

        with open('data.csv', 'w', newline='') as csvfile:
            count = 0
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(['Team Name', 'Year', 'Wins', 'Losses'])
            for row in table.xpath('.//tr'):
                if count > 100:
                    break
                try:
                    team_name = row.xpath('.//td[1]/text()').get(default='')
                    year = row.xpath('.//td[2]/text()').get(default='')
                    wins = row.xpath('.//td[3]/text()').get(default='')
                    losses = row.xpath('.//td[4]/text()').get(default='')
                    count += 1
                    writer.writerow([team_name, year, wins, losses])
                except IndexError:
                    pass
