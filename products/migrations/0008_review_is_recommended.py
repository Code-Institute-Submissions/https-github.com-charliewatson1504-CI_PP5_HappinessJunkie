# Generated by Django 3.2.13 on 2022-08-03 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_review_star_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='is_recommended',
            field=models.BooleanField(blank=True, default=None, null=True),
        ),
    ]
