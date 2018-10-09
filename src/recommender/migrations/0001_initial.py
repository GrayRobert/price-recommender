# Generated by Django 2.1.2 on 2018-10-09 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModelTrainingHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accuracy_r2', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PricePrediction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('predicted_price', models.FloatField(null=True)),
            ],
        ),
    ]
