# Generated by Django 2.1 on 2018-09-06 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20180906_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='logo',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='subject',
            name='thumbail',
            field=models.CharField(default='', max_length=100),
        ),
    ]
