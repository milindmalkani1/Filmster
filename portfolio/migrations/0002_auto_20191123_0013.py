# Generated by Django 2.2.6 on 2019-11-22 18:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='phone',
            field=models.CharField(max_length=15, null=True, validators=[django.core.validators.RegexValidator(message='Phone number entered must be in a valid format.', regex='^(?:\\s+|)((0|(?:(\\+|)91))(?:\\s|-)*(?:(?:\\d(?:\\s|-)*\\d{9})|(?:\\d{2}(?:\\s|-)*\\d{8})|(?:\\d{3}(?:\\s|-)*\\d{7}))|\\d{10})(?:\\s+|)$')]),
        ),
    ]
