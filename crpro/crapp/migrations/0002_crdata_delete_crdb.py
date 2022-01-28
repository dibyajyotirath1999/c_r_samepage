# Generated by Django 4.0 on 2022-01-27 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='crdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('course', models.CharField(max_length=100)),
                ('fee', models.FloatField()),
                ('sub1', models.CharField(max_length=100)),
                ('sub2', models.CharField(max_length=100)),
                ('sub3', models.CharField(max_length=100)),
                ('sub4', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='crdb',
        ),
    ]
