# Generated by Django 2.2.6 on 2019-10-23 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('price', models.DecimalField(decimal_places=2, default=1.99, max_digits=2, max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('price', models.DecimalField(decimal_places=2, default=4.99, max_digits=2, max_length=4)),
                ('size', models.CharField(max_length=12)),
                ('toppings', models.ManyToManyField(null=True, to='pizza.Topping')),
            ],
        ),
    ]