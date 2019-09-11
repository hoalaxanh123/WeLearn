# Generated by Django 2.1 on 2018-09-06 18:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20180906_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='logo',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subject',
            name='thumbail',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='catID',
            field=models.IntegerField(verbose_name='Category ID'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(verbose_name='Content '),
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(verbose_name='Description '),
        ),
        migrations.AlterField(
            model_name='post',
            name='viewCount',
            field=models.IntegerField(default='0', editable=False, verbose_name='View count '),
        ),
    ]
