# Generated by Django 5.2 on 2025-04-15 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MAIN', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='landrequest',
            name='city',
        ),
        migrations.RemoveField(
            model_name='landrequest',
            name='country',
        ),
        migrations.RemoveField(
            model_name='landrequest',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='landrequest',
            name='door_no',
        ),
        migrations.RemoveField(
            model_name='landrequest',
            name='state',
        ),
        migrations.AddField(
            model_name='landrequest',
            name='area_name',
            field=models.CharField(default='N/A', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='landrequest',
            name='land_area',
            field=models.CharField(default='N/A', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='landrequest',
            name='land_country',
            field=models.CharField(default='N/A', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='landrequest',
            name='land_district',
            field=models.CharField(default='N/A', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='landrequest',
            name='land_state',
            field=models.CharField(default='N/A', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='landrequest',
            name='user_area',
            field=models.CharField(default='N/A', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='landrequest',
            name='user_country',
            field=models.CharField(default='N/A', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='landrequest',
            name='user_district',
            field=models.CharField(default='N/A', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='landrequest',
            name='user_door_no',
            field=models.CharField(default='N/A', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='landrequest',
            name='user_state',
            field=models.CharField(default='N/A', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='landrequest',
            name='additional_details',
            field=models.TextField(default='N/A'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='landrequest',
            name='land_required_sqft',
            field=models.IntegerField(),
        ),
    ]
