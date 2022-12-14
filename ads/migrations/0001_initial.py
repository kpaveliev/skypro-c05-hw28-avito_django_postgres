# Generated by Django 4.1 on 2022-08-17 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('lat', models.DecimalField(decimal_places=6, max_digits=8)),
                ('lng', models.DecimalField(decimal_places=6, max_digits=8)),
            ],
            options={
                'verbose_name': 'Местоположение',
                'verbose_name_plural': 'Местоположения',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=150)),
                ('username', models.CharField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=200)),
                ('role', models.CharField(choices=[('admin', 'администратор'), ('member', 'пользователь'), ('moderator', 'модератор')], default='member', max_length=10)),
                ('age', models.SmallIntegerField()),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ads.location')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=30)),
                ('price', models.PositiveIntegerField(default=0)),
                ('description', models.TextField(max_length=2000)),
                ('address', models.CharField(max_length=200)),
                ('is_published', models.BooleanField(default=None)),
                ('image', models.ImageField(upload_to='logos/')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ads.category')),
            ],
            options={
                'verbose_name': 'Объявление',
                'verbose_name_plural': 'Объявления',
            },
        ),
    ]
