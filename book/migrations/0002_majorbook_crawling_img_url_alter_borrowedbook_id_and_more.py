# Generated by Django 4.0 on 2021-12-25 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='majorbook',
            name='crawling_img_url',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='borrowedbook',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='majorbook',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
