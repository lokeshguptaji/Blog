# Generated by Django 3.0.8 on 2021-08-14 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_Blog', '0002_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]