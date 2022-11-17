# Generated by Django 3.2.13 on 2022-11-17 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_alter_comment_movie_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='movie_rate',
            field=models.CharField(choices=[('★', '★'), ('★☆', '★☆'), ('★★', '★★'), ('★★☆', '★★☆'), ('★★★', '★★★'), ('★★★☆', '★★★☆'), ('★★★★', '★★★★'), ('★★★★☆', '★★★★☆'), ('★★★★★', '★★★★★')], default='★', max_length=5),
        ),
    ]
