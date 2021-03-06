# Generated by Django 3.1.7 on 2021-04-10 09:24

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('CourseId', models.AutoField(primary_key=True, serialize=False)),
                ('Title', models.CharField(max_length=30)),
                ('Hours', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('InstructorId', models.AutoField(primary_key=True, serialize=False)),
                ('First_name', models.CharField(max_length=20)),
                ('Last_name', models.CharField(max_length=20)),
                ('Gender', models.CharField(choices=[('1', 'Male'), ('2', 'Female')], max_length=10)),
                ('Address', models.CharField(max_length=20)),
                ('mobileNo', phonenumber_field.modelfields.PhoneNumberField(max_length=128, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('StudentId', models.AutoField(primary_key=True, serialize=False)),
                ('First_name', models.CharField(max_length=20)),
                ('Last_name', models.CharField(max_length=20)),
                ('Password', models.CharField(max_length=30)),
                ('RegYear', models.DateField()),
                ('Gender', models.CharField(choices=[('1', 'Male'), ('2', 'Female')], max_length=10)),
                ('Address', models.CharField(max_length=20)),
                ('mobileNo', phonenumber_field.modelfields.PhoneNumberField(max_length=128, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('SectionNo', models.IntegerField(primary_key=True, serialize=False)),
                ('RoomNo', models.IntegerField()),
                ('Time', models.TimeField()),
                ('CourseId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Reg_admin.course')),
                ('InstructorId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Reg_admin.instructor')),
            ],
        ),
    ]
