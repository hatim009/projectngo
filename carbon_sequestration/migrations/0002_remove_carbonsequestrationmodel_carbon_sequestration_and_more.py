# Generated by Django 4.2.7 on 2024-01-29 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carbon_sequestration', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carbonsequestrationmodel',
            name='carbon_sequestration',
        ),
        migrations.RemoveField(
            model_name='carbonsequestrationmodel',
            name='id',
        ),
        migrations.RemoveField(
            model_name='carbonsequestrationmodel',
            name='total_pits_dug',
        ),
        migrations.RemoveField(
            model_name='carbonsequestrationmodel',
            name='total_pits_fertilized',
        ),
        migrations.RemoveField(
            model_name='carbonsequestrationmodel',
            name='total_pits_planted',
        ),
        migrations.RemoveField(
            model_name='carbonsequestrationmodel',
            name='total_pits_target',
        ),
        migrations.AddField(
            model_name='carbonsequestrationmodel',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='carbonsequestrationmodel',
            name='model',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='CarbonSequestrationProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_pits_target', models.IntegerField()),
                ('total_pits_dug', models.IntegerField(default=0)),
                ('total_pits_fertilized', models.IntegerField(default=0)),
                ('total_pits_planted', models.IntegerField(default=0)),
                ('carbon_sequestration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='progress', to='carbon_sequestration.carbonsequestration')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='models', to='carbon_sequestration.carbonsequestrationmodel')),
            ],
            options={
                'db_table': 'carbon_sequestration_progress',
            },
        ),
    ]
