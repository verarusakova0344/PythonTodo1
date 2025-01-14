# Generated by Django 4.1.3 on 2022-12-15 09:34

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('email_verify', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Workspaces',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_workspace', models.CharField(max_length=50, verbose_name='Название РП')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('describe_workspace', models.TextField(blank=True, verbose_name='Описание РП')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Создатель')),
            ],
            options={
                'verbose_name': 'Рабочие пространства',
                'verbose_name_plural': 'Рабочие пространства',
                'ordering': ['user_id', 'id'],
            },
        ),
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_workspace', models.BooleanField(verbose_name='Редактор')),
                ('id_workspace', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Todo.workspaces', verbose_name='Рабочее пространство')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Доступ к рабочим пространствам',
                'verbose_name_plural': 'Доступ к рабочим пространствам',
                'ordering': ['user_id', 'id'],
            },
        ),
        migrations.CreateModel(
            name='Columns',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_column', models.CharField(max_length=50, verbose_name='Название Колонки')),
                ('describe_column', models.TextField(blank=True, verbose_name='Описание колонки')),
                ('id_workspace', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Todo.workspaces')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Создатель')),
            ],
            options={
                'verbose_name': 'Готовые доски',
                'verbose_name_plural': 'Готовые доски',
                'ordering': ['user_id', 'id'],
            },
        ),
        migrations.CreateModel(
            name='Cards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_card', models.CharField(max_length=50, verbose_name='Название задания')),
                ('describe_card', models.TextField(blank=True, verbose_name='Описание задания')),
                ('date_card', models.DateTimeField(verbose_name='Дата выполнения задания')),
                ('isdo_card', models.BooleanField(verbose_name='Задание выполнено?')),
                ('id_column', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Todo.columns', verbose_name='Айди колонки')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Задания',
                'verbose_name_plural': 'Задания',
                'ordering': ['user_id', 'id'],
            },
        ),
    ]
