# Generated by Django 2.0 on 2018-06-14 20:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20180614_1930'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='nicname',
        ),
    ]
