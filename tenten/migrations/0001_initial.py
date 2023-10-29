# Generated by Django 4.1.3 on 2023-10-29 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recommend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_link', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('title', models.CharField(max_length=200)),
                ('dc_rate', models.IntegerField()),
                ('reply_cnt', models.IntegerField()),
                ('like_cnt', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': '텐x텐 웹스크래핑',
            },
        ),
    ]
