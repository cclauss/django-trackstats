# Generated by Django 4.0.4 on 2022-04-24 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trackstats', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domain',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='metric',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='statisticbydate',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='statisticbydateandobject',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
