# Generated by Django 3.1.5 on 2021-01-16 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20210115_2325'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectportfolio',
            name='photo2',
            field=models.ImageField(blank=True, upload_to='photos_project2/%Y/%m/%d', verbose_name='Картинка вторая'),
        ),
        migrations.AddField(
            model_name='projectportfolio',
            name='photo3',
            field=models.ImageField(blank=True, upload_to='photos_project3/%Y/%m/%d', verbose_name='Картинка третья'),
        ),
    ]
