# Generated by Django 3.0.7 on 2020-07-02 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200630_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itempricehist',
            name='active_status_prsnl_id',
            field=models.BigIntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='trans_action',
            name='comment',
            field=models.TextField(blank=True, default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='trans_action',
            name='event_tag',
            field=models.CharField(blank=True, default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='trans_action',
            name='event_title',
            field=models.CharField(blank=True, default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='transcomment',
            name='comment',
            field=models.TextField(blank=True, default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='transevent',
            name='event_id',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='transitem',
            name='comment',
            field=models.CharField(blank=True, default=' ', max_length=255),
            preserve_default=False,
        ),
    ]