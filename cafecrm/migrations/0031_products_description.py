# Generated by Django 4.1.4 on 2023-01-10 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafecrm', '0030_alter_products_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
