# Generated by Django 3.2.9 on 2022-01-20 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booksmodel',
            name='jenis_buku',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='booksmodel',
            name='penerbit',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='booksmodel',
            name='penulis',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='booksmodel',
            name='tahun_terbit',
            field=models.DateField(),
        ),
    ]
