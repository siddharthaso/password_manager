# Generated by Django 3.2.13 on 2022-05-15 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0005_alter_site_is_public'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='is_public',
            field=models.BooleanField(default=True),
        ),
    ]
