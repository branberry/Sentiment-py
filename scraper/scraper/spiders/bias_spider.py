import scrapy

class BiasSpider(scrapy.Spider):
    name = "bias"

    def start_requests(self):
        urls = [
            'https://mediabiasfactcheck.com/left/',
            'https://mediabiasfactcheck.com/leftcenter/',
            'https://mediabiasfactcheck.com/center/',
            'https://mediabiasfactcheck.com/right-center/',
            'https://mediabiasfactcheck.com/right/',
            'https://mediabiasfactcheck.com/pro-science/',
            'https://mediabiasfactcheck.com/conspiracy/',

        ]
        for url in urls:
            yield scrapy.Request(url, callback=self.parse)
    
    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'sites-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)