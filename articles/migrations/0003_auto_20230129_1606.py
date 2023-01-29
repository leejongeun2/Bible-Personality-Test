# Generated by Django 3.2.13 on 2023-01-29 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20230126_2333'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mbti',
            name='hits',
        ),
        migrations.RemoveField(
            model_name='question',
            name='alphabet',
        ),
        migrations.AddField(
            model_name='question',
            name='answer1_letter',
            field=models.CharField(default='I', max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='answer2_letter',
            field=models.CharField(default='E', max_length=1),
            preserve_default=False,
        ),
    ]