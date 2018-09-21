import scrapy
class testLabSpider(scrapy.Spider):
	"""docstring for testLabSpider"""
	name = "quotes"
	start_urls = [
		'http://lab.scrapyd.cn',
	]

	def parse(self, response):
		for quote in response.css('div.quote'):
			yield {
				'内容': quote.css('span.text::text').extract_first().decode(),
				'作者': quote.xpath('span/small/text()').extract_first().decode(),
			}

		next_page = response.css('li.next a::attr("href")').extract_first()
		if next_page is not None:
			yield scrapy.Request(next_page, self.parse)
