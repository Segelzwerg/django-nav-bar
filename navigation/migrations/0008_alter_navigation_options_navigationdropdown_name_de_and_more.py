# Generated by Django 5.0.6 on 2024-05-11 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navigation', '0007_navigation_name_de_navigation_name_en_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='navigation',
            options={'verbose_name': 'Navigation', 'verbose_name_plural': 'Navigations'},
        ),
        migrations.AddField(
            model_name='navigationdropdown',
            name='name_de',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='navigationdropdown',
            name='name_en',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='navigationlogo',
            name='alt_text_de',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='navigationlogo',
            name='alt_text_en',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='navigationlogo',
            name='name_de',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='navigationlogo',
            name='name_en',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='navigation',
            name='order',
            field=models.IntegerField(default=0, verbose_name='order'),
        ),
    ]
