# Generated by Django 3.2.8 on 2023-03-30 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=100)),
                ('team_record', models.CharField(max_length=10)),
                ('team_id', models.IntegerField()),
            ],
        ),
    ]
