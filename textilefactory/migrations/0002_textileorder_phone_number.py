# Generated by Django 4.1.7 on 2023-06-06 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('textilefactory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='textileorder',
            name='phone_number',
            field=models.PositiveIntegerField(default=1, unique=True, verbose_name='Номер телефона'),
            preserve_default=False,
        ),
    ]
