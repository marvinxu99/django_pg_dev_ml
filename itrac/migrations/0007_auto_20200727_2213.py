# Generated by Django 3.0.7 on 2020-07-28 05:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('itrac', '0006_auto_20200727_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savedissue',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_savedissues', to=settings.AUTH_USER_MODEL),
        ),
    ]
