# Generated by Django 4.2.1 on 2023-05-28 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userplan',
            old_name='user_plan',
            new_name='user',
        ),
    ]