# Generated by Django 5.0.7 on 2024-09-08 14:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0008_rename_user_booking_author_rename_user_review_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='TourGroupDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_size', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TourThemes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_themes', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TourType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('with_gid', models.BooleanField()),
                ('description', models.TextField()),
                ('country', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='air_codinting',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='car',
            name='car_style',
            field=models.CharField(default='sedan', max_length=50),
        ),
        migrations.AddField(
            model_name='car',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='car',
            name='wifi',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='car',
            name='year',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tour',
            name='duration',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='tour',
            name='group_detail',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tour.tourgroupdetail'),
        ),
        migrations.AddField(
            model_name='tour',
            name='themes',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tour.tourthemes'),
        ),
        migrations.AddField(
            model_name='tour',
            name='tour_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tour.tourtype'),
        ),
    ]
