# Generated by Django 3.1.4 on 2021-01-13 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='solution',
            name='sol_number',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='author',
            name='slug',
            field=models.SlugField(default=models.CharField(max_length=50)),
        ),
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=models.SlugField(default=models.CharField(max_length=100)),
        ),
    ]
