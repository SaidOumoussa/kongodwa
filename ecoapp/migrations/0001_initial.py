# Generated by Django 3.1.5 on 2021-12-08 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categorie', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=85)),
                ('price', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('description', models.TextField(max_length=150)),
                ('active', models.BooleanField(default=True)),
                ('service', models.BooleanField(default=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='Product_img')),
            ],
        ),
        migrations.CreateModel(
            name='Product_img',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_img', models.ImageField(upload_to='media/image', verbose_name='image')),
                ('active', models.BooleanField(default=True)),
                ('product_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecoapp.product')),
            ],
        ),
    ]