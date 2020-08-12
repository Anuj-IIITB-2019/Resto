# Generated by Django 3.0.8 on 2020-07-23 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=500)),
                ('people', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('preperation_time', models.IntegerField()),
                ('image', models.ImageField(upload_to='meals/')),
            ],
        ),
    ]
