# Generated by Django 3.2.7 on 2021-09-22 00:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('simulados', '0007_alter_questao_simulado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questao',
            name='simulado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simulados.simulado'),
        ),
    ]
