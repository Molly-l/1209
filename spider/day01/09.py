# # <div class="animal">.*?title="(.*?)".*?
#
#  <div class="animal">
#  <p class="name">
#  <a title="Tiger"></a>
#  </p>
#  <p class="content">
#  Two tigers two tigers run fast
#
# </p>
# </div>


from urllib import parse, request  # 将汉字转换成url编码

a='恐惧和'
b=parse.quote(a)
c=parse.urlencode({'wd':a})

resp=request.urlopen()










#
# <div class="animal">12 <p class="name">
#  <a title="Rabbit"></a>
#  </p>
#
#  <p class="content">
#  Small white rabbit white and white
#
# </p>
# </div>