# Generated by Django 4.2.16 on 2024-12-03 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='exerpt',
            field=models.TextField(blank=True),
        ),
    ]
