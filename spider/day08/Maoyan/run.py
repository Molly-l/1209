from scrapy import cmdline

# cmdline.execute('scrapy crawl maoyan2'.split())
cmdline.execute('scrapy crawl maoyan2 -o maoyan.csv'.split())