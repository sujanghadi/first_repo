# Generated by Django 3.0.2 on 2020-02-03 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20200131_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]