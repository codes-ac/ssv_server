# Generated by Django 3.1.4 on 2021-02-11 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_notice_board_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice_board',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]