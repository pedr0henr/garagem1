# Generated by Django 4.1.7 on 2023-03-31 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Garagem', '0003_remove_marca_site_marca_nacionalidade_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acessorios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
            options={
                'verbose_name_plural': 'Autores',
            },
        ),
    ]
