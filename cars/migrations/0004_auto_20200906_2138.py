# Generated by Django 2.2.13 on 2020-09-06 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_auto_20200906_0641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='img'),
        ),
    ]
