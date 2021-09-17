# Generated by Django 3.2.7 on 2021-09-17 00:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('height', models.PositiveIntegerField()),
                ('weight', models.PositiveIntegerField()),
                ('pokemon_id', models.PositiveIntegerField(unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('prevolution', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prevolutions', to='command.pokemon', verbose_name='prevolution')),
            ],
        ),
        migrations.CreateModel(
            name='Stat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=40)),
                ('base_stat', models.IntegerField(default=0)),
                ('pokemon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='command.pokemon')),
            ],
        ),
    ]