# Generated by Django 3.1.1 on 2020-09-06 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0010_auto_20200906_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatsessionmessage',
            name='text',
            field=models.TextField(max_length=2000, null=True),
        ),
    ]