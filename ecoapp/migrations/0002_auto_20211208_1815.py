# Generated by Django 3.1.5 on 2021-12-08 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecoapp', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Categorie',
        ),
        migrations.RemoveField(
            model_name='product',
            name='title',
        ),
        migrations.AddField(
            model_name='product',
            name='product',
            field=models.CharField(blank=True, max_length=89),
        ),
        migrations.DeleteModel(
            name='Product_img',
        ),
    ]
