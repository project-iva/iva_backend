# Generated by Django 3.2.5 on 2021-10-01 17:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_remove_default_uuid_for_healthkit_models'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bodymass',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='mindfulsession',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='sleepanalysis',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='traininginstance',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
