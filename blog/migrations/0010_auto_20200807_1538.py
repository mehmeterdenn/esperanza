# Generated by Django 3.0.8 on 2020-08-07 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20200807_1343'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogcategory',
            old_name='level',
            new_name='mptt_level',
        ),
    ]
