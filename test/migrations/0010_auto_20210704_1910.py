# Generated by Django 3.2.5 on 2021-07-04 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test', '0009_url_urltitle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repository',
            name='title',
            field=models.CharField(default='New Repo title', max_length=50),
        ),
        migrations.AlterField(
            model_name='webmark',
            name='title',
            field=models.CharField(default='New WebMark Title', max_length=50),
        ),
    ]