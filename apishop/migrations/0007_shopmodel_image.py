# Generated by Django 5.0.1 on 2024-01-18 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apishop', '0006_shopmodel_detail'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopmodel',
            name='image',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]