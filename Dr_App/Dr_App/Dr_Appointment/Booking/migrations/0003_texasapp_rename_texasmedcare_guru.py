# Generated by Django 4.0.6 on 2022-08-26 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0002_rename_mohan_texasmedcare'),
    ]

    operations = [
        migrations.CreateModel(
            name='texasapp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('age', models.CharField(max_length=50)),
                ('box', models.CharField(max_length=200)),
                ('dob', models.DateField(max_length=50)),
                ('number', models.CharField(max_length=12)),
                ('add', models.CharField(max_length=100)),
                ('tp', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameModel(
            old_name='texasmedcare',
            new_name='guru',
        ),
    ]
