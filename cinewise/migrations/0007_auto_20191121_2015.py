# Generated by Django 2.2.7 on 2019-11-21 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinewise', '0006_delete_person'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinput',
            name='nodes',
        ),
        migrations.AddField(
            model_name='userinput',
            name='nodes',
            field=models.ManyToManyField(to='cinewise.Node'),
        ),
    ]