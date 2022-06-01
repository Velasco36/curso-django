# Generated by Django 4.0.4 on 2022-05-26 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0004_skills_alter_employee_options_alter_employee_job_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'ordering': ['-first_name', 'last_name'], 'verbose_name': 'my employee'},
        ),
        migrations.AlterModelOptions(
            name='skills',
            options={'verbose_name': 'Ability', 'verbose_name_plural': 'Employee Skills'},
        ),
        migrations.AlterField(
            model_name='employee',
            name='job',
            field=models.CharField(choices=[('3', 'OTRO'), ('1', 'ADMINISTRADOR'), ('0', 'CONTADOR'), ('2', 'ECONOMISTA')], max_length=1, verbose_name='job'),
        ),
    ]
