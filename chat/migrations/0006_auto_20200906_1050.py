# Generated by Django 3.1.1 on 2020-09-06 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_chatsessionmessage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatsessionmessage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='chat/'),
        ),
    ]
