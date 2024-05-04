# Generated by Django 5.0.2 on 2024-03-04 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('date', models.DateField(auto_now_add=True)),
                ('hour', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]