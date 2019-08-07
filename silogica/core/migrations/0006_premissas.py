# Generated by Django 2.2.4 on 2019-08-07 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_delete_premissas'),
    ]

    operations = [
        migrations.CreateModel(
            name='PREMISSAS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modo', models.CharField(max_length=40)),
                ('reducao', models.CharField(max_length=40)),
                ('extensao1', models.CharField(max_length=20)),
                ('termo1', models.CharField(max_length=100)),
                ('n1', models.CharField(max_length=4)),
                ('termo2', models.CharField(max_length=100)),
                ('extensao2', models.CharField(max_length=20)),
                ('termo3', models.CharField(max_length=100)),
                ('n2', models.CharField(max_length=4)),
                ('termo4', models.CharField(max_length=100)),
                ('extensao3', models.CharField(max_length=20)),
                ('termo5', models.CharField(max_length=100)),
                ('n3', models.CharField(max_length=4)),
                ('termo6', models.CharField(max_length=100)),
            ],
        ),
    ]