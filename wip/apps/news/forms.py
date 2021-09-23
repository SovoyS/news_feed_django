from .models import News
from django.forms import ModelForm, Textarea, ImageField


class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['news_title', 'news_text', 'news_image']
        widgets = {
            "news_title": Textarea(attrs={
                'class': 'title_style',
                'placeholder': 'Заголовок новости',
                'required': 'True',

            }),
            "news_text": Textarea(attrs={
                'class': 'text_style',
                'placeholder': 'Текст новости',
                'required': 'True'
            }),

        }
