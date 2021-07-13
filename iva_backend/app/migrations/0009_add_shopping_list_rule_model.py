# Generated by Django 3.2.3 on 2021-07-13 19:49

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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_threshold', models.FloatField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.measurableitem')),
            ],
        ),
        migrations.AddConstraint(
            model_name='shoppinglistrule',
            constraint=models.UniqueConstraint(fields=('item',), name='unique_item_rule'),
        ),
    ]
