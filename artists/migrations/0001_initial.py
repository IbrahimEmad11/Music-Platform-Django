# Generated by Django 4.1.2 on 2022-11-02 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage_name', models.CharField(max_length=30, unique=True)),
                ('social_link', models.URLField(blank=True)),
            ],
            options={
                'ordering': ['stage_name'],
            },
        ),
    ]
