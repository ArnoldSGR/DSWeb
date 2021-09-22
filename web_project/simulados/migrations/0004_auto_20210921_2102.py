# Generated by Django 3.2.7 on 2021-09-22 00:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('simulados', '0003_auto_20210921_1954'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='simulado',
            name='questoes',
        ),
        migrations.AddField(
            model_name='questao',
            name='simulado',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='simulados.simulado'),
        ),
    ]
