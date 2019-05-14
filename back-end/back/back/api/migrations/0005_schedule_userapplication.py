# Generated by Django 2.2 on 2019-05-14 05:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0004_auto_20190512_1547'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=200)),
                ('recruiter_contact', models.CharField(max_length=200)),
                ('applied_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Position')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Status')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_type', models.CharField(max_length=200)),
                ('date', models.DateTimeField()),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
