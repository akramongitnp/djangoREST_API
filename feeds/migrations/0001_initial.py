# Generated by Django 4.0.3 on 2022-07-26 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('content', models.TextField(max_length=200)),
                ('author', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
