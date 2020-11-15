# Generated by Django 3.1 on 2020-11-14 21:15

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_add_intent_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainingInstance',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('message_text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('intent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='training_instances', to='app.intent')),
            ],
        ),
    ]
