# Generated by Django 4.0.5 on 2022-07-02 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_remove_user_username_alter_user_email'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
            ],
        ),
        migrations.AddField(
            model_name='chairman',
            name='fullname',
            field=models.CharField(default='test chairman', max_length=150),
        ),
    ]
