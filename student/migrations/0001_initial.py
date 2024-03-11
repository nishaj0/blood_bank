# Generated by Django 3.2.23 on 2024-02-05 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.AutoField(primary_key=True, serialize=False)),
                ('admission_no', models.CharField(max_length=45)),
                ('name', models.CharField(max_length=45)),
                ('course', models.CharField(max_length=45)),
                ('year', models.CharField(max_length=45)),
                ('phone', models.CharField(max_length=45)),
                ('dob', models.DateField()),
                ('username', models.CharField(max_length=45)),
                ('password', models.CharField(max_length=45)),
                ('bloodgroup', models.CharField(max_length=45)),
                ('status', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'student',
                'managed': False,
            },
        ),
    ]
