# Generated by Django 2.1.7 on 2019-03-11 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0008_auto_20190311_0256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='marks',
            field=models.IntegerField(default=(1, 2, 3, 4, 5, 6, 7, 8, 9)),
        ),
    ]
