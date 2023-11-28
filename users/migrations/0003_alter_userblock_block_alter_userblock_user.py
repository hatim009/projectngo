# Generated by Django 4.2.7 on 2023-11-28 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('local_directories', '0001_initial'),
        ('users', '0002_alter_userblock_block'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userblock',
            name='block',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='local_directories.blocksdirectory'),
        ),
        migrations.AlterField(
            model_name='userblock',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assigned_blocks', to='users.user'),
        ),
    ]
