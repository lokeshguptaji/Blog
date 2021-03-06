# Generated by Django 3.0.8 on 2021-08-03 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('login_count', models.PositiveIntegerField(default=0)),
                ('last_login', models.DateTimeField()),
                ('timestamps', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
