# Generated by Django 4.0.3 on 2022-03-19 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apply', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicantForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=200)),
                ('mobile', models.CharField(max_length=15)),
                ('education', models.CharField(max_length=50)),
                ('exp', models.CharField(max_length=50)),
                ('resume', models.FileField(upload_to='uploads/%Y/%m/%d/')),
            ],
        ),
        migrations.DeleteModel(
            name='Job_apply',
        ),
    ]
