# Generated by Django 2.0 on 2017-12-28 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='items_content',
            field=models.TextField(verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='items_data',
            field=models.DateField(blank=True, null=True, verbose_name='日期'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='items_isFinish',
            field=models.BooleanField(default=True, verbose_name='已完成'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='items_time',
            field=models.TimeField(blank=True, null=True, verbose_name='时间'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='items_title',
            field=models.CharField(max_length=256, verbose_name='标题'),
        ),
    ]