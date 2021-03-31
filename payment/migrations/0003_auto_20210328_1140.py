# Generated by Django 3.1.7 on 2021-03-28 06:10

import django.core.serializers.json
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_auto_20210327_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='action_required_data',
            field=models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='gateway_response',
            field=models.JSONField(encoder=django.core.serializers.json.DjangoJSONEncoder),
        ),
    ]