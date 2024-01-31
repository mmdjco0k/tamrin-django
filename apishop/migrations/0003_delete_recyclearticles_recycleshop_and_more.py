# Generated by Django 5.0.1 on 2024-01-16 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apishop', '0002_shopmodel_title'),
    ]

    operations = [
        migrations.DeleteModel(
            name='RecycleArticles',
        ),
        migrations.CreateModel(
            name='RecycleShop',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('apishop.shopmodel',),
        ),
        migrations.AlterField(
            model_name='shopmodel',
            name='is_deleted',
            field=models.BooleanField(default=False, null=True),
        ),
    ]