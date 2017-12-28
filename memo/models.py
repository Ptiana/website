from django.db import models

# Create your models here.

class Schedule(models.Model):
    items_title = models.CharField('标题',max_length=256)
    items_content = models.TextField('内容')
    items_data = models.DateField('日期',null=True, blank=True)
    items_time = models.TimeField('时间', null=True, blank=True)
    items_isFinish = models.BooleanField('已完成', default=True)

