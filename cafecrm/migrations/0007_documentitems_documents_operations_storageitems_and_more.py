# Generated by Django 4.1.4 on 2022-12-28 17:12

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cafecrm', '0006_order_orderitem_product_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(verbose_name='Количество')),
            ],
            options={
                'verbose_name': 'Товар в документе',
                'verbose_name_plural': 'Товары в документе',
            },
        ),
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания')),
                ('update_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата изменения')),
                ('to_remove', models.BooleanField(default=False, verbose_name='Помечен на удаление')),
                ('document_type', models.CharField(choices=[('income', 'Приход'), ('expense', 'Расход')], max_length=10, verbose_name='Тип документа')),
                ('apply_flag', models.BooleanField(default=False, verbose_name='Документ проведен')),
            ],
            options={
                'verbose_name': 'Документ',
                'verbose_name_plural': 'Документы',
                'ordering': ['-create_date'],
            },
        ),
        migrations.CreateModel(
            name='Operations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=200, null=True, verbose_name='Пользователь')),
                ('operation', models.TextField(verbose_name='Операция')),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата и время операции')),
            ],
            options={
                'verbose_name': 'Операция',
                'verbose_name_plural': 'Операции',
                'ordering': ['-create_date'],
            },
        ),
        migrations.CreateModel(
            name='StorageItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания')),
                ('update_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата изменения')),
                ('to_remove', models.BooleanField(default=False, verbose_name='Помечен на удаление')),
                ('count', models.IntegerField(verbose_name='Количество')),
                ('item', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='cafecrm.goods', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Остаток',
                'verbose_name_plural': 'Остатки',
            },
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='order',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='product',
        ),
        migrations.AlterIndexTogether(
            name='product',
            index_together=None,
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.AddField(
            model_name='documentitems',
            name='document',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cafecrm.documents', verbose_name='Документ'),
        ),
        migrations.AddField(
            model_name='documentitems',
            name='good',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cafecrm.goods', verbose_name='Товар'),
        ),
    ]
