# Generated by Django 2.0.3 on 2018-04-29 07:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('polls', '0008_auto_20180428_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrationdetails',
            name='registration_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='details',
                                    to='polls.Registration'),
        ),
    ]
