# Generated by Django 3.2.4 on 2021-07-07 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='other_colors',
            field=models.ManyToManyField(related_name='colors', to='shop.Colors'),
        ),
    ]