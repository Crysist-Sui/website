# Generated by Django 2.0.12 on 2019-11-25 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0019_auto_20191125_1029'),
    ]

    operations = [
        migrations.AddField(
            model_name='forum',
            name='is_type',
            field=models.BooleanField(default=False, verbose_name='是否隐藏可见'),
        ),
    ]
