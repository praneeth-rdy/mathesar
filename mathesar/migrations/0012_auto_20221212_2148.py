# Generated by Django 3.1.14 on 2022-12-12 21:48

import django.contrib.postgres.fields
from django.db import migrations, models
import mathesar.models.query


class Migration(migrations.Migration):

    dependencies = [
        ('mathesar', '0011_auto_20221208_2303'),
    ]

    operations = [
        migrations.AddField(
            model_name='tablesettings',
            name='column_order',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), default=None, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='uiquery',
            name='display_names',
            field=models.JSONField(blank=True, null=True, validators=[mathesar.models.query._get_validator_for_dict]),
        ),
        migrations.AlterField(
            model_name='uiquery',
            name='display_options',
            field=models.JSONField(blank=True, null=True, validators=[mathesar.models.query._get_validator_for_dict]),
        ),
        migrations.AlterField(
            model_name='uiquery',
            name='initial_columns',
            field=models.JSONField(validators=[mathesar.models.query._get_validator_for_list_of_dicts, mathesar.models.query._get_validator_for_initial_columns]),
        ),
        migrations.AlterField(
            model_name='uiquery',
            name='transformations',
            field=models.JSONField(blank=True, null=True, validators=[mathesar.models.query._get_validator_for_list_of_dicts, mathesar.models.query._get_validator_for_transformations]),
        ),
    ]
