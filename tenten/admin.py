from django.contrib import admin
from tenten.models import Recommend

# Register your models here.

class RecommendAdmin(admin.ModelAdmin):
    fieldsets = [
        ('image_link', {'fields' : ['image_link']}),
        ('link', {'fields' : ['link']}),
        ('price', {'fields' : ['price']}),
        ('title', {'fields' : ['title']}),
        ('dc_rate', {'fields' : ['dc_rate']}),
        ('reply_cnt', {'fields' : ['reply_cnt']}),
        ('like_cnt', {'fields' : ['like_cnt']}),
    ]
    list_display = ('image_link', 'link', 'price', 'title', 'dc_rate', 'reply_cnt', 'like_cnt')
admin.site.register(Recommend, RecommendAdmin)