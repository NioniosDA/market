# Generated by Django 2.0 on 2018-09-11 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diagnostics', '0031_auto_20180911_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagnosticsquestionnaire',
            name='Management_10',
            field=models.IntegerField(choices=[(1, 'No'), (2, float("nan")), (3, float("nan")), (4, 'Yes')], default=1),
        ),
        migrations.AlterField(
            model_name='diagnosticsquestionnaire',
            name='Processes_0',
            field=models.IntegerField(choices=[(1, 'No'), (2, float("nan")), (3, float("nan")), (4, 'Yes')], default=1),
        ),
        migrations.AlterField(
            model_name='diagnosticsquestionnaire',
            name='Processes_1',
            field=models.IntegerField(choices=[(1, 'No - not applicable'), (2, float("nan")), (3, float("nan")), (4, 'Yes')], default=1),
        ),
    ]
