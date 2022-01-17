# Generated by Django 4.1.dev20211229065945 on 2022-01-05 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('mail', models.EmailField(max_length=355)),
                ('city', models.CharField(choices=[('Mumbai', 'Mumbai'), ('Delhi', 'Delhi'), ('Chennai', 'Chennai'), ('Banglore', 'Banglore'), ('Kolkata', 'Kolkata')], max_length=400)),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]