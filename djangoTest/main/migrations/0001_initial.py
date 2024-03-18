# Generated by Django 4.2.9 on 2024-02-19 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('picture', models.CharField(max_length=200)),
                ('vize', models.BooleanField()),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Town',
            fields=[
                ('id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('id_country', models.CharField(max_length=200)),
            ],
        ),
    ]