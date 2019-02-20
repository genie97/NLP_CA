# Generated by Django 2.1.5 on 2019-02-20 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviewtext', models.TextField()),
                ('sentsum', models.CharField(max_length=255)),
                ('pos', models.FloatField()),
                ('neut', models.FloatField()),
                ('neg', models.FloatField()),
                ('emosum', models.CharField(max_length=255)),
                ('happy', models.FloatField()),
                ('angry', models.FloatField()),
                ('excited', models.FloatField()),
                ('sad', models.FloatField()),
                ('bored', models.FloatField()),
                ('afraid', models.FloatField()),
                ('disgust', models.FloatField()),
                ('keyword1', models.CharField(max_length=255)),
                ('keyword2', models.CharField(max_length=255)),
                ('keyword3', models.CharField(max_length=255)),
            ],
        ),
    ]
