# Generated by Django 2.0 on 2018-06-16 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kpi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='graphdata_business',
            name='user',
        ),
        migrations.RemoveField(
            model_name='graphdata_follower',
            name='user',
        ),
        migrations.AddField(
            model_name='exceltemplate',
            name='period',
            field=models.CharField(choices=[('y', 'Year'), ('m', 'Month')], default='y', max_length=10),
        ),
        migrations.DeleteModel(
            name='GraphData_business',
        ),
        migrations.DeleteModel(
            name='GraphData_follower',
        ),
    ]
