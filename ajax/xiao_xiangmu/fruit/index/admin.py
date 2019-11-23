from django.contrib import admin

# Register your models here.
from index.models import Goods, GoodsType


class GoodsAdmin(admin.ModelAdmin):
    list_display =('title','goodsType','price','spec','isActive')
    list_filter=('title','isActive')
    search_fields = ('title',)
    list_editable = ('price','spec')

admin.site.register(GoodsType)
admin.site.register(Goods,GoodsAdmin)

