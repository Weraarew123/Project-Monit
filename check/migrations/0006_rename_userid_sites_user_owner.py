# Generated by Django 4.2.9 on 2024-02-02 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('check', '0005_alter_sites_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sites',
            old_name='userId',
            new_name='user_owner',
        ),
    ]