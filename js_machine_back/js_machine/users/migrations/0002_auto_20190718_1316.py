# Generated by Django 2.2.2 on 2019-07-18 13:16

from django.db import migrations, models
import js_machine.users.models
import js_machine.users.validations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={},
        ),
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', js_machine.users.models.UserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='user',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
        migrations.AddField(
            model_name='user',
            name='about_skills',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='birthday',
            field=models.DateField(null=True, validators=[js_machine.users.validations.validate_birthday]),
        ),
        migrations.AddField(
            model_name='user',
            name='company',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='full_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=js_machine.users.models.get_user_photo_path),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(db_index=True, max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(db_index=True, error_messages={'unique': 'A user with that username already exists'}, max_length=50, unique=True, validators=[js_machine.users.validations.UsernameValidator()]),
        ),
    ]
