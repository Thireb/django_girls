# Generated by Django 4.1.3 on 2022-11-28 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_feedbackpost'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FeedbackPost',
        ),
    ]
