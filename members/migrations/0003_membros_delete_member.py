# Generated by Django 5.0 on 2023-12-08 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_member_joined_date_member_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Membros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('sobrenome', models.CharField(max_length=255)),
                ('idade', models.IntegerField(default=0)),
                ('numero', models.IntegerField(null=True)),
                ('email', models.EmailField(max_length=255)),
                ('dataEntrada', models.DateField(null=True)),
                ('numeroMembro', models.IntegerField(null=True)),
                ('categoria', models.CharField(max_length=255)),
                ('vitorias', models.IntegerField(null=0)),
                ('derrotas', models.IntegerField(null=0)),
            ],
        ),
        migrations.DeleteModel(
            name='Member',
        ),
    ]
