# Generated by Django 2.1.7 on 2019-03-22 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apiv2', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='book',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
    ]
