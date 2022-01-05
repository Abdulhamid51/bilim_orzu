# Generated by Django 3.2.8 on 2021-12-30 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BrithDays',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Ismi')),
                ('day', models.DateField(verbose_name='Tugilgan kuni')),
                ('image', models.ImageField(blank=True, upload_to='birday_user/', verbose_name='Rasmi')),
            ],
        ),
    ]