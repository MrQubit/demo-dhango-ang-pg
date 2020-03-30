# Generated by Django 3.0.4 on 2020-03-30 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=70)),
                ('age', models.IntegerField(default=1)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
    ]
