# Generated by Django 4.2.9 on 2024-01-18 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
