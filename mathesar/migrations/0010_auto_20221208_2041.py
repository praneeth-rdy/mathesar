# Generated by Django 3.1.14 on 2022-12-08 20:41

from django.db import migrations, models
import mathesar.models.query


class Migration(migrations.Migration):

    dependencies = [
        ('mathesar', '0009_auto_20221123_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password_change_needed',
            field=models.BooleanField(default=True),
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
