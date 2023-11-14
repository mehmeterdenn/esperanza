# Generated by Django 3.0.8 on 2020-08-05 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200805_2010'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='slidercontent',
            new_name='preview',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='writer',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]