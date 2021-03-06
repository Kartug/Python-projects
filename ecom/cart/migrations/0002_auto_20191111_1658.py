# Generated by Django 2.2 on 2019-11-11 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='purchased',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='orderId',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='paymentId',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
