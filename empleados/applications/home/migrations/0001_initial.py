# Generated by Django 4.0.4 on 2022-05-24 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('caption', models.CharField(max_length=50)),
                ('amount', models.IntegerField()),
            ],
        ),
    ]
