# Generated by Django 3.2.6 on 2021-09-02 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_alter_news_news_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='news_image',
            field=models.ImageField(blank=True, default='images/image.jpg', null=True, upload_to='images/', verbose_name=''),
        ),
    ]
