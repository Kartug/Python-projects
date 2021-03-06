# Generated by Django 2.2 on 2019-11-09 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20191108_1158'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('primaryCategory', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='image_url',
        ),
        migrations.AddField(
            model_name='product',
            name='detail_text',
            field=models.TextField(default='', max_length=1000, verbose_name='Detail Text'),
        ),
        migrations.AddField(
            model_name='product',
            name='mainimage',
            field=models.ImageField(blank=True, null=True, upload_to='products/'),
        ),
        migrations.AddField(
            model_name='product',
            name='preview_text',
            field=models.TextField(default='', max_length=200, verbose_name='Preview Text'),
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=''),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default='', editable=False, on_delete=django.db.models.deletion.CASCADE, to='products.Category'),
        ),
    ]
