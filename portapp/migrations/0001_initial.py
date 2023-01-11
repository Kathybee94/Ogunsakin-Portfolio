# Generated by Django 3.2.13 on 2022-12-28 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('content', models.TextField(max_length=500)),
                ('image', models.ImageField(blank=True, null=True, upload_to='upload/pics')),
            ],
        ),
        migrations.CreateModel(
            name='resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone_num', models.IntegerField()),
                ('content', models.TextField(max_length=1000)),
            ],
        ),
    ]