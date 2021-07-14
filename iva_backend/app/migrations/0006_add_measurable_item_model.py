# Generated by Django 3.2.3 on 2021-07-13 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('app', '0005_add_sleep_analysis_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='MeasurableItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('amount', models.FloatField()),
                ('unit', models.CharField(choices=[('ML', 'ml'), ('MG', 'mg'), ('PACKAGE', 'package')], max_length=7)),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_app.measurableitem_set+', to='contenttypes.contenttype')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
    ]