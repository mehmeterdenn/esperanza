# Generated by Django 3.0.8 on 2020-08-07 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20200807_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='blog.BlogPost', verbose_name='parent'),
        ),
    ]
