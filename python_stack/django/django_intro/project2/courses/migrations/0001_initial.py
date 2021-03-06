# Generated by Django 2.2.4 on 2022-06-26 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DescText', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseName', models.CharField(max_length=64)),
                ('created_at', models.DateTimeField()),
                ('courseDesc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='courses.Description')),
            ],
        ),
    ]
