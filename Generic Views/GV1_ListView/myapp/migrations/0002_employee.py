# Generated by Django 4.0.2 on 2022-04-14 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('eno', models.CharField(max_length=5)),
                ('course', models.CharField(max_length=20)),
            ],
        ),
    ]