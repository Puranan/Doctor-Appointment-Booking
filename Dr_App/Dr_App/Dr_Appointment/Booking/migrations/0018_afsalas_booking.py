# Generated by Django 4.0.6 on 2023-04-13 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0017_senthil_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='afsalas_Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NAME1', models.CharField(blank=True, default=True, max_length=10)),
            ],
        ),
    ]
