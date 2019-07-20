# Generated by Django 2.2.2 on 2019-07-08 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Synthetica', '0003_generate'),
    ]

    operations = [
        migrations.AddField(
            model_name='generate',
            name='data_type',
            field=models.CharField(choices=[('t', 'Short Text'), ('n', 'Numeric'), ('a', 'Alphanumeric'), ('lt', 'Long Text')], default='t', max_length=2, verbose_name='Data Type'),
        ),
        migrations.AddField(
            model_name='generate',
            name='options',
            field=models.TextField(default='1,2,3', max_length=100, verbose_name='Options:'),
        ),
    ]