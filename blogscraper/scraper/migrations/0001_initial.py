# Generated by Django 2.2.4 on 2019-08-08 07:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_name', models.CharField(max_length=40)),
                ('blog_url', models.URLField()),
                ('date_added', models.DateField(auto_now_add=True)),
                ('subscribers', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=40)),
                ('date_added', models.DateField(auto_now=True)),
                ('blog_title', models.CharField(max_length=40)),
                ('blog_text', models.TextField(max_length=5000)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scraper.Blog')),
            ],
        ),
    ]
