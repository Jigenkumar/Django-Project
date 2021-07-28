# Generated by Django 3.2.5 on 2021-07-23 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_reviews'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('msg', models.CharField(max_length=200)),
                ('rate', models.CharField(max_length=20)),
                ('satisfied', models.CharField(max_length=20)),
                ('prices', models.CharField(max_length=20)),
                ('support', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Reviews',
        ),
    ]