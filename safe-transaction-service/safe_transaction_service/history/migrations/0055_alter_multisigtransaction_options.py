# Generated by Django 4.0.2 on 2022-03-07 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("history", "0054_webhook_authorization"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="multisigtransaction",
            options={
                "permissions": [("create_trusted", "Can create trusted transactions")]
            },
        ),
    ]