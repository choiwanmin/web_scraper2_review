from django.db import models
from django.utils.timezone import now

# Create your models here.

class Recommend(models.Model):
    image_link = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    price = models.IntegerField()
    title = models.CharField(max_length=200)
    dc_rate = models.IntegerField()
    reply_cnt = models.IntegerField()
    like_cnt = models.IntegerField()

    class Meta:
        verbose_name_plural = "텐x텐 웹스크래핑"
    def __str__(self):
        return f'{self.link}--{self.price}--{self.title}--{self.dc_rate}--{self.reply_cnt}--{self.like_cnt}'