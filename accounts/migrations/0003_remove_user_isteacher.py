# Generated by Django 3.1.4 on 2021-03-12 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_isteacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='isTeacher',
        ),
    ]
