# Generated by Django 3.2.23 on 2024-02-05 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CampRequest',
            fields=[
                ('request_id', models.AutoField(primary_key=True, serialize=False)),
                ('request', models.CharField(max_length=45)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('status', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'camp_request',
                'managed': True,
            },
        ),
    ]
