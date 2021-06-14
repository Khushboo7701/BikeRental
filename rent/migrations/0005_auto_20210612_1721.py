# Generated by Django 3.2.3 on 2021-06-12 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0004_auto_20210608_2217'),
    ]

    operations = [
        migrations.AddField(
            model_name='bike',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='bike',
            name='img',
            field=models.ImageField(null=True, upload_to='pics'),
        ),
        migrations.AlterField(
            model_name='bike',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='bike',
            name='price',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='rent',
            name='amount',
            field=models.IntegerField(default=0),
        ),
    ]
