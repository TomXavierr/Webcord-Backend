# Generated by Django 4.2.4 on 2023-11-06 16:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("server", "0003_servermember_join_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="servermember",
            name="join_date",
            field=models.DateField(auto_now_add=True),
        ),
    ]
