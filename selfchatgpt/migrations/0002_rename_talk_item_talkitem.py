# Generated by Django 5.0.6 on 2024-06-12 16:15

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("login", "0001_initial"),
        ("selfchatgpt", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Talk_item",
            new_name="TalkItem",
        ),
    ]
