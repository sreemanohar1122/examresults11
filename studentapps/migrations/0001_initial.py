# Generated by Django 4.2.2 on 2023-06-20 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('roll_no', models.IntegerField()),
                ('telugu', models.IntegerField(default=0)),
                ('maths', models.IntegerField(default=0)),
                ('stat', models.IntegerField(default=0)),
                ('science', models.IntegerField(default=0)),
                ('total', models.IntegerField(default=0)),
                ('percent', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
