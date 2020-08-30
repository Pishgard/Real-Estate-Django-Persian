# Generated by Django 3.0.7 on 2020-08-12 10:05

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0002_realtor_photo_main'),
        ('listings', '0002_auto_20200812_1349'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150)),
                ('address', models.TextField()),
                ('bathroom', models.IntegerField(default=1)),
                ('bedroom', models.IntegerField(default=1)),
                ('infr', models.CharField(blank=True, max_length=100)),
                ('details', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_published', models.BooleanField(default=True)),
                ('list_date', models.DateTimeField(blank=True, default=datetime.datetime(2020, 8, 12, 14, 35, 27, 114571))),
                ('photo_main', models.ImageField(upload_to='photos/%Y/%M/%D/')),
                ('photo_1', models.ImageField(upload_to='photos/%Y/%M/%D/')),
                ('photo_2', models.ImageField(upload_to='photos/%Y/%M/%D/')),
                ('realtor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='realtors.Realtor')),
            ],
        ),
        migrations.DeleteModel(
            name='Listing',
        ),
    ]