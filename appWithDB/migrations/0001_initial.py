# Generated by Django 4.2.2 on 2024-02-01 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_title', models.CharField(max_length=255)),
                ('category_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='coatings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coating_category', models.IntegerField()),
                ('coating_name', models.CharField(max_length=128)),
                ('coating_vendor_code', models.CharField(max_length=128)),
                ('coating_ral', models.CharField(max_length=128)),
                ('coating_preview', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_user_id', models.IntegerField()),
                ('order_user_name', models.CharField(max_length=128)),
                ('order_user_phone', models.CharField(max_length=64)),
                ('order_user_email', models.CharField(max_length=128)),
                ('order_price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='panel_size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('panel_size_category', models.IntegerField()),
                ('panel_size_vendor_code', models.CharField(max_length=128)),
                ('panel_size_size', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='panel_thickness',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('panel_thickness_category', models.IntegerField()),
                ('panel_thickness_vendor_code', models.CharField(max_length=128)),
                ('panel_thickness_thickness', models.FloatField()),
            ],
        ),
    ]
