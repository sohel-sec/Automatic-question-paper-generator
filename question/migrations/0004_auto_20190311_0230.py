# Generated by Django 2.1.7 on 2019-03-10 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0003_auto_20190311_0210'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='access_modifier',
            field=models.CharField(choices=[('PUBLIC', 'PUBLIC'), ('POTECTED', 'POTECTED'), ('PRIVATE', 'PRIVATE')], default='PUBLIC', max_length=8),
        ),
        migrations.AddField(
            model_name='questions',
            name='marks',
            field=models.IntegerField(default=2),
        ),
        migrations.AddField(
            model_name='questions',
            name='question_text',
            field=models.TextField(default='What ?'),
        ),
    ]
