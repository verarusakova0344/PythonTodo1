from django.contrib.auth.models import User, AbstractUser
from django.db import models
from slugify import slugify
from django.urls import reverse

from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    email= models.EmailField(_
                             ('email address'),
                             unique=True,)
    email_verify = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

# рабочие пространства
class Workspaces(models.Model):
    name_workspace = models.CharField(max_length=50, verbose_name="Название РП")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    describe_workspace = models.TextField(blank=True, verbose_name="Описание РП")
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Создатель")


    def __str__(self):
        return self.name_workspace
        return self.describe_workspace

    def save(self, *args, **kwargs):
        self.slug = slugify( self.name_workspace)
        return super(Workspaces, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('task', kwargs={'workspace_slug': self.slug})

    def get_update_ws(self):
        return reverse('update_workspace', kwargs={'workspace_slug': self.slug})

    def get_update_column(self):
        return reverse('update_column', kwargs={ 'id': self.id})

    def get_update_task(self):
        return reverse('update_task', kwargs={ 'id': self.id})

    def get_add_column_url(self):
        return reverse('add_column', kwargs={'workspace_slug': self.slug})

    def get_add_task_url(self):
        return reverse('add_task', kwargs={'workspace_slug': self.slug})

    class Meta:
        verbose_name='Рабочие пространства'
        verbose_name_plural='Рабочие пространства'
        ordering=['user_id', 'id']



class Columns(models.Model):
    name_column = models.CharField(max_length=50, verbose_name="Название Колонки")
    describe_column = models.TextField(blank=True, verbose_name="Описание колонки")
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Создатель")
    id_workspace = models.ForeignKey(Workspaces, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_column
        return self.describe_column

    class Meta:
        verbose_name='Готовые доски'
        verbose_name_plural='Готовые доски'
        ordering=['user_id', 'id']

class Cards(models.Model):
    name_card = models.CharField(max_length=50, verbose_name="Название задания")
    describe_card = models.TextField(blank=True, verbose_name="Описание задания")
    date_card = models.DateTimeField(verbose_name="Дата выполнения задания")
    isdo_card = models.BooleanField( verbose_name="Задание выполнено?")
    id_column = models.ForeignKey(Columns, on_delete=models.CASCADE, verbose_name="Айди колонки")
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")

    def __str__(self):
        return self.name_card
        return self.describe_card
        return self.date_card
        return self.time_card
        return self.isdo_card

    class Meta:
        verbose_name='Задания'
        verbose_name_plural='Задания'
        ordering=['user_id', 'id']



class Members(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь" )
    id_workspace = models.ForeignKey(Workspaces, on_delete=models.CASCADE, verbose_name="Рабочее пространство")
    access_workspace = models.BooleanField(verbose_name="Редактор")

    class Meta:
        verbose_name = 'Доступ к рабочим пространствам'
        verbose_name_plural = 'Доступ к рабочим пространствам'
        ordering = ['user_id', 'id']
