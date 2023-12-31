# Generated by Django 3.0.8 on 2020-07-27 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_setting'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='contact',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='setting',
            name='aboutus',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='setting',
            name='address',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='setting',
            name='email',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='setting',
            name='facebook',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='setting',
            name='fax',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='setting',
            name='instagram',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='setting',
            name='phone',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='setting',
            name='references',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='setting',
            name='smtpemail',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='setting',
            name='smtpserver',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='setting',
            name='twitter',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='setting',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
