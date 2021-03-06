# Generated by Django 3.1.7 on 2021-04-13 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Reg_admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Grads', models.IntegerField(null=True)),
                ('CourseId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Reg_admin.course')),
                ('SectionNo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Reg_admin.section')),
                ('StudentId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Reg_admin.student')),
            ],
        ),
    ]
