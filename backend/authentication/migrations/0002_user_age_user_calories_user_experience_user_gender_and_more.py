# Generated by Django 4.0.4 on 2022-05-15 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='calories',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='experience',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='goal',
            field=models.CharField(max_length=75, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='height',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='is_employee',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='weight',
            field=models.IntegerField(null=True),
        ),
    ]
