import random
import time
from urllib import request
from fake_useragent import UserAgent  # 可以在线生成一个User-Agent请求头
import re
import csv

class MaoYan:
    def get_html(self):




    def save_html(self,film_list):
        with open('fmaoyan.csv', 'a') as f:  # with语句中f自动关闭, 'a'追加
            writer=csv.writer(f)
            for film in film_list:



    def run(self):
        for offset in range(0,91,10):
            url=self.url.format(offset)
            self.get_html(url)
            #
            time.sleep(random.uniform(0,1))
        self.cursor.close()
        self.db.close()



if __name__ == '__main__':
    start=time.time()
    spider=
    spider
