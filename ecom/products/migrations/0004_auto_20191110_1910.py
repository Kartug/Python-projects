# Generated by Django 2.2 on 2019-11-10 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20191110_0039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default='1', editable=False, on_delete=django.db.models.deletion.CASCADE, to='products.Category'),
        ),
    ]
