# Generated by Django 5.0.7 on 2024-08-11 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0007_rename_author_booking_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='user',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='user',
            new_name='author',
        ),
    ]
