# Generated by Django 3.2.5 on 2021-09-29 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_add_nutrition_info_to_ingredient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bodymass',
            name='uuid',
            field=models.UUIDField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='mindfulsession',
            name='uuid',
            field=models.UUIDField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='sleepanalysis',
            name='uuid',
            field=models.UUIDField(primary_key=True, serialize=False),
        ),
    ]
