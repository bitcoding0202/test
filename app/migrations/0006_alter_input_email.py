# Generated by Django 4.1.2 on 2022-11-10 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_input_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='input',
            name='email',
            field=models.EmailField(max_length=100, unique=True),
        ),
    ]
