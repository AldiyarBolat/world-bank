# Generated by Django 2.0.6 on 2019-05-12 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20190512_1542'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='firstName',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='lastName',
        ),
    ]
