# Generated by Django 4.0.4 on 2022-05-22 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_alter_user_goal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='experience',
            field=models.IntegerField(choices=[(1, 'Beginner'), (2, 'Intermediate'), (3, 'Advanced')], null=True),
        ),
    ]
