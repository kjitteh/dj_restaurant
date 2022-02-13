# Generated by Django 4.0.2 on 2022-02-13 07:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='eg. pizza, pasta', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('people', models.PositiveSmallIntegerField()),
                ('date', models.DateTimeField()),
                ('message', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('recipe', models.CharField(max_length=100)),
                ('tag', models.CharField(blank=True, choices=[('h', 'hot!'), ('p', 'popular'), ('s', 'special')], max_length=1, null=True)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizza.menu')),
            ],
            options={
                'verbose_name_plural': 'Dishes',
            },
        ),
    ]
