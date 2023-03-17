# Generated by Django 4.1.7 on 2023-03-17 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Garagem', '0002_marca'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='marca',
            name='site',
        ),
        migrations.AddField(
            model_name='marca',
            name='nacionalidade',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='marca',
            name='nome',
            field=models.CharField(max_length=50),
        ),
    ]
