# Generated by Django 3.2.13 on 2022-11-09 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('overview', models.TextField()),
                ('release_date', models.TextField()),
                ('poster_path', models.TextField()),
                ('vote_average', models.TextField()),
                ('director', models.TextField()),
                ('wise_saying', models.TextField()),
            ],
        ),
    ]
