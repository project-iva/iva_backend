# Generated by Django 3.1.3 on 2020-11-29 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_add_intent_and_training_instance_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='traininginstance',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
