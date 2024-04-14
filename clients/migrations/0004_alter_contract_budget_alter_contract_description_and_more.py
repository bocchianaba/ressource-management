# Generated by Django 5.0.4 on 2024-04-14 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_rename_contract_duration_contract_duration_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='budget',
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='contract',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='contract',
            name='duration',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='contract',
            name='max_changes',
            field=models.BigIntegerField(default=0),
        ),
    ]
