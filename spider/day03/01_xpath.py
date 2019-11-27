from lxml import etree


html = '''
<div class="wrapper">
	<a href="/" id="channel">新浪社会</a>
	<ul id="nav">
		<li><a href="http://domestic.sina.com/" title="国内">国内</a></li>
		<li><a href="http://world.sina.com/" title="国际">国际</a></li>
		<li><a href="http://mil.sina.com/" title="军事">军事</a></li>
		<li><a href="http://photo.sina.com/" title="图片">图片</a></li>
		<li><a href="http://society.sina.com/" title="社会">社会</a></li>
		<li><a href="http://ent.sina.com/" title="娱乐">娱乐</a></li>
		<li><a href="http://tech.sina.com/" title="科技">科技</a></li>
		<li><a href="http://sports.sina.com/" title="体育">体育</a></li>
		<li><a href="http://finance.sina.com/" title="财经">财经</a></li>
		<li><a href="http://auto.sina.com/" title="汽车">汽车</a></li>
	</ul>
</div>
'''
p = etree.HTML(html)
r_list = p.xpath('//a/text()')

# 匹配 国内 国际 军事 ,不包含 新浪社会
p = etree.HTML(html)
xpath_bds = '//div[@class="wrapper"]/ul//a/text()'
r_list = p.xpath(xpath_bds)

# 1.匹配所有的a节点中 href 的属性值
r_list = p.xpath('//a/@href')
# print(r_list)

# 2. ['http://xxx','http://xxx'] 不包含 '/'
xpath_bds = '//ul[@id="nav"]/li/a/@href'
r_list = p.xpath(xpath_bds)
# print(r_list)

# 考虑一下能否使用 contains() 函数实现
xpath_bds = '//a[contains(@href,"http")]/@href'
r_list = p.xpath(xpath_bds)
for r in r_list:
    print(r)











