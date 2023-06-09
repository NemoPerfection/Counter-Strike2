from django.db import models
from datetime import datetime


class Post(models.Model):
    #pk = PrimarykeyField()
    title = models.CharField("Заголовок", max_length=255, null=True)
    content = models.TextField("Контент", null=True, blank=True)
    postDate = models.DateTimeField("Дата и время публикации", default=datetime.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
