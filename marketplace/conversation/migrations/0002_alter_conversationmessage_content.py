# Generated by Django 4.2 on 2023-04-18 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conversation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversationmessage',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
