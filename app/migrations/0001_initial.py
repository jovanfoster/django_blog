# Generated by Django 3.1 on 2020-08-24 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('date_created', models.TimeField(auto_now=True)),
            ],
        ),
    ]
