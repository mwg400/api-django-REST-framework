# Generated by Django 3.0.8 on 2020-07-13 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('language', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Courses',
        ),
    ]
