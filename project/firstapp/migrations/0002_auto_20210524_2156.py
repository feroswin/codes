# Generated by Django 3.2.1 on 2021-05-24 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'ordering': ['-created_at'], 'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AlterField(
            model_name='products',
            name='content',
            field=models.TextField(blank=True, verbose_name='Контент'),
        ),
        migrations.AlterField(
            model_name='products',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='products',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Статус опубликования'),
        ),
        migrations.AlterField(
            model_name='products',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фотография'),
        ),
        migrations.AlterField(
            model_name='products',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='products',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Обновление'),
        ),
    ]
