from django.db import models

class products(models.Model):
    title = models.CharField(max_length = 100, verbose_name = "Наименование")
    content = models.TextField(blank = True, verbose_name = "Контент")
    created_at = models.DateTimeField(auto_now_add = True, verbose_name = "Дата публикации")
    updated_at = models.DateTimeField(auto_now = True, verbose_name = "Обновление")
    photo = models.ImageField(upload_to = "photos/%Y/%m/%d/", verbose_name = "Фотография", blank = True)
    is_published = models.BooleanField(default = True, verbose_name = "Статус опубликования")

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ["-created_at",]
