# Generated by Django 3.2.3 on 2021-07-14 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_add_meal_tracker_entry_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShoppingListRule',
            fields=[
                ('item', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='app.measurableitem')),
                ('amount_threshold', models.FloatField()),
                ('amount_to_purchase', models.FloatField()),
            ],
        ),
    ]
