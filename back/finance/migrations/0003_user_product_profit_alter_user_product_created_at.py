# Generated by Django 4.2.8 on 2024-05-22 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0002_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_product',
            name='profit',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user_product',
            name='created_at',
            field=models.DateTimeField(),
        ),
    ]
