# Generated by Django 3.1.4 on 2021-04-23 08:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CheckIn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('day', models.CharField(max_length=255, null=True)),
                ('time', models.CharField(max_length=50, null=True)),
                ('user_id', models.IntegerField(null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, null=True)),
            ],
            options={
                'db_table': 'checkin',
            },
        ),
        migrations.CreateModel(
            name='CheckOut',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('day', models.CharField(max_length=255, null=True)),
                ('time', models.CharField(max_length=50, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, null=True)),
            ],
            options={
                'db_table': 'checkout',
            },
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('email', models.CharField(max_length=255, null=True)),
                ('message', models.CharField(max_length=1000, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, null=True)),
            ],
            options={
                'db_table': 'contact_us',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(max_length=255, null=True)),
                ('employee_email', models.CharField(max_length=255, null=True)),
                ('employee_phone', models.IntegerField(null=True)),
                ('employee_password', models.CharField(max_length=255, null=True)),
                ('employee_address', models.CharField(max_length=255, null=True)),
                ('image', models.FileField(null=True, upload_to='')),
                ('employee_latitude', models.CharField(max_length=255, null=True)),
                ('employee_longitude', models.CharField(max_length=255, null=True)),
                ('employee_gender', models.BooleanField(default=True, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, null=True)),
            ],
            options={
                'db_table': 'employees',
            },
        ),
        migrations.CreateModel(
            name='RequestDemo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('company_name', models.CharField(max_length=255, null=True)),
                ('email', models.CharField(max_length=255, null=True)),
                ('phone', models.IntegerField(null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, null=True)),
            ],
            options={
                'db_table': 'request_demo',
            },
        ),
    ]
