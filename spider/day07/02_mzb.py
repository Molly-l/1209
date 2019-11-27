from selenium import webdriver

class GovSpider(object):
    def __init__(self):
        options=webdriver.ChromeOptions()
        options.add_argument('')

        self.browser=webdriver.Chrome()
        self.one_url = ''

    def get_incr_url(self):
        self.browser.get(self.one_url)
        # 提取最新链接节点对象并点击
        self.browser.find_element_by_xpath(
            '//td[@class="arlisttd"]/a[contains(@title,"代码")]'
        ).click()
        # 获取当前所有句柄(窗口)
        all_handles = self.browser.window_handles
        # 切换browser到新的窗口,获取新窗口的对象
        self.browser.switch_to.window(all_handles[1])
        self.get_data()

    def get_data(self):
        tr_list=self.browser.find_elements_by_xpath('')
        for tr in tr_list:
            code=tr.find_element_by_xpath('./td[2]').text.strip()
            name=tr.find_element_by_xpath('./td[3]').text.strip()




    def run(self):
        self.get_incr_url()

        self.browser.quit()

if __name__ == '__main__':
    spider = GovSpider()
    spider.run()