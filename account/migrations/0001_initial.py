# Generated by Django 4.1.7 on 2023-06-01 02:05

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(blank=True, max_length=255, null=True, unique=True, verbose_name='Электронная почта')),
                ('username', models.CharField(max_length=50, unique=True, verbose_name='Имя')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True, verbose_name='Номер телефона')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активен аккаунт?')),
                ('is_admin', models.BooleanField(default=False, verbose_name='Админ?')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
