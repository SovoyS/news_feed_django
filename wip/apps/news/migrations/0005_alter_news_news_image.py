# Generated by Django 3.2.6 on 2021-09-02 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20210902_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='news_image',
            field=models.ImageField(blank=True, default='images/image.jpg', null=True, upload_to='images/'),
        ),
    ]
