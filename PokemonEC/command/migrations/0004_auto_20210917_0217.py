# Generated by Django 3.2.7 on 2021-09-17 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('command', '0003_alter_pokemon_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='prevolution',
            field=models.ManyToManyField(related_name='_command_pokemon_prevolution_+', to='command.Pokemon', verbose_name='prevolution'),
        ),
        migrations.AlterUniqueTogether(
            name='pokemon',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='pokemon',
            name='prevolution',
        ),
    ]
