# Generated by Django 3.2.13 on 2022-05-15 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0006_alter_site_is_public'),
    ]

    operations = [
        migrations.RenameField(
            model_name='site',
            old_name='is_public',
            new_name='is_private',
        ),
    ]
