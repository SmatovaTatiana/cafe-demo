# Generated by Django 4.1.4 on 2023-01-10 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cafecrm', '0029_document_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'ordering': ['product_type', 'product_name'], 'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
    ]