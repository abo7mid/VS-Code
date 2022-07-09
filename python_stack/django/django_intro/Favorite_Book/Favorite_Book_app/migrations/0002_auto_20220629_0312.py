# Generated by Django 2.2.4 on 2022-06-29 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Favorite_Book_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='full_name',
            new_name='email',
        ),
        migrations.AddField(
            model_name='user',
            name='firstname',
            field=models.CharField(default='Muhammed', max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='lastname',
            field=models.CharField(default='Alnadawy', max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default=12345678, max_length=64),
            preserve_default=False,
        ),
    ]