from django.db import models


class News(models.Model):
    news_title = models.CharField('', max_length=150)
    news_text = models.TextField('')
    news_image = models.ImageField('', null=True, blank=True, upload_to='images/', default='images/image.jpg')
    date = models.DateTimeField('Дата публикации', auto_now_add=True)
