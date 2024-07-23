# Generated by Django 5.0.6 on 2024-07-23 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_product_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Test',
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('phone', 'phone'), ('tab', 'tab'), ('labtop', 'labtop')], default='cat', max_length=50, null=True),
        ),
    ]
