# Generated by Django 4.0.4 on 2022-05-26 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='job',
            field=models.CharField(choices=[('0', 'CONTADOR'), ('2', 'ECONOMISTA'), ('3', 'OTRO'), ('1', 'ADMINISTRADOR')], max_length=1, verbose_name='job'),
        ),
    ]
