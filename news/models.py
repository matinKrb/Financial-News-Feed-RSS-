from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'دسته بندی',
        verbose_name_plural = 'دسته بندی ها'

class NewsSource(models.Model):
    name = models.CharField(max_length=200)
    rss_url = models.URLField(unique=True )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE ,
        related_name='news_source'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "منبع خبری"
        verbose_name_plural = "منابع خبری"


class News(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='news'
    )
    source = models.ForeignKey(
        NewsSource,
        on_delete=models.CASCADE,
        related_name='items'
    )

    title = models.CharField(max_length=200)
    link = models.URLField(unique=True  )
    summary = models.TextField(blank=True)
    published = models.CharField(max_length=100, blank=True)
    fetched_at = models.DateTimeField(auto_now_add=True )

    class Meta:
        verbose_name = "خبر"
        verbose_name_plural = "اخبار"
        ordering = ['-published']

    def __str__(self):
        return self.title


