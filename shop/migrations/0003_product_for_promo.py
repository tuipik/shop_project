# Generated by Django 2.2.3 on 2019-08-05 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20190801_2233'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='for_promo',
            field=models.BooleanField(default=False),
        ),
    ]
