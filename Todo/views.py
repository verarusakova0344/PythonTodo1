from datetime import date, time, datetime

from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.core.exceptions import ValidationError
from django.http import HttpResponseNotFound, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.http import urlsafe_base64_decode
from django.utils.timezone import now
from django.views import View
from django.views.generic import ListView, CreateView
from django.contrib.auth.tokens import default_token_generator as token_generator

from Todo.forms import UserCreationForm, AuthenticationForm, AddWorkspace, AddColumn, AddTask, AddAccess

from Todo.models import *
from Todo.utils import send_email_for_verify

User = get_user_model()

class MyLoginView(LoginView):
    form_class = AuthenticationForm

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

# class WorkspaceHome(LoginRequiredMixin, ListView):
#     model = Workspaces
#     template_name = 'workspaces/workspaces.html'
#     context_object_name ='posts'
#     login_url = reverse_lazy('home')
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title']='Рабочие пространства'
#         return context
#     def get_queryset(self):
#         return Workspaces.objects.all()
# выбирает конретные записи для выведения на экран


class WorkspaceHome(LoginRequiredMixin, ListView):
    template_name = 'workspaces/workspaces.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Рабочие пространства'
        return context

    def get(self, request):
        posts = Workspaces.objects.all()
        members = Members.objects.all()
        return render(request, 'workspaces/workspaces.html',
                      {'posts': posts,  'members': members, })


def index(request):
    return render(request, "mainpage/index.html")

def lk(request):
    return HttpResponse( "Личный кабинет")


class TaskHome(ListView):
    template_name = 'tasks/tasks.html'
    context_object_name = 'columns'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']='Задание'
        return context

    def get(self, request, workspace_slug):
            posts = Workspaces.objects.filter(slug=workspace_slug)
            columns = Columns.objects.filter(id_workspace__slug=self.kwargs['workspace_slug'])
            cards = Cards.objects.all()
            members = Members.objects.all()
            return render(request, "tasks/tasks.html", {'posts': posts, 'columns': columns, 'cards': cards, 'members': members,})

    def account_view(request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))

        return render(request)


class TaskHomeNeed(ListView):
    template_name = 'tasks/tasks.html'
    context_object_name = 'columns'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']='Задание'
        return context

    def get(self, request, workspace_slug):
            posts = Workspaces.objects.filter(slug=workspace_slug)
            columns = Columns.objects.filter(id_workspace__slug=self.kwargs['workspace_slug'])
            cards = Cards.objects.filter(isdo_card=False)
            members = Members.objects.all()
            return render(request, "tasks/tasks.html", {'posts': posts, 'columns': columns, 'cards': cards, 'members': members,})
    def account_view(request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))

        return render(request)
class TaskHomeIs(ListView):
    template_name = 'tasks/tasks.html'
    context_object_name = 'columns'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']='Задание'
        return context

    def get(self, request, workspace_slug):
            posts = Workspaces.objects.filter(slug=workspace_slug)
            columns = Columns.objects.filter(id_workspace__slug=self.kwargs['workspace_slug'])
            cards = Cards.objects.filter(isdo_card=True)
            members = Members.objects.all()
            return render(request, "tasks/tasks.html", {'posts': posts, 'columns': columns, 'cards': cards, 'members': members,})
    def account_view(request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))

        return render(request)
class TaskHomeTime(ListView):
    template_name = 'tasks/tasks.html'
    context_object_name = 'columns'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']='Задание'
        return context

    def get(self, request, workspace_slug):
            posts = Workspaces.objects.filter(slug=workspace_slug)
            columns = Columns.objects.filter(id_workspace__slug=self.kwargs['workspace_slug'])
            cards = Cards.objects.filter(isdo_card=False).exclude(date_card__gte=datetime.now())
            members = Members.objects.all()
            return render(request, "tasks/tasks.html", {'posts': posts, 'columns': columns, 'cards': cards, 'members': members,})
    def account_view(request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))

        return render(request)

class Add_ws(CreateView):
    form_class = AddWorkspace
    template_name = 'workspaces/addworkspace.html'
    success_url = reverse_lazy('workspace')

    def form_valid(self, form):
        form.instance.user_id = self.request.user
        return super(Add_ws, self).form_valid(form)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']='Создать рабочее пространство'
        return context

class Add_access(CreateView):
    form_class = AddAccess
    template_name = 'workspaces/add_access.html'
    success_url = reverse_lazy('workspace')


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']='Предоставить доступ к рабочим пространствам'
        return context

class Add_column(CreateView):
    form_class = AddColumn
    template_name = 'tasks/addcolumn.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title']='Создать новую колонку'
        return context


    def post(self, request, *args, **kwargs):
        wsslug= self.kwargs['workspace_slug']
        form = AddColumn(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user_id = request.user

            post.save()


        return redirect('task', wsslug)

    def account_view(request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        return redirect(request)


class Add_task(CreateView):
    form_class = AddTask
    template_name = 'tasks/addtask.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создать новую карточку'
        return context

    def post(self, request, *args, **kwargs):
        wsslug = self.kwargs['workspace_slug']
        form = AddTask(request.POST)
        if form.is_valid():
            form.save()

        return redirect('task', wsslug)

    def account_view(request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        return redirect(request)

class Edit_ws(CreateView):
   def get(self, request,workspace_slug):
       tag = Workspaces.objects.get(slug__iexact=workspace_slug)
       bound_form = AddWorkspace(instance=tag)
       return render(request, 'workspaces/ws_edit.html', context={'form':bound_form, 'tag':tag})

   def post(self, request, workspace_slug):
       tag = Workspaces.objects.get(slug__iexact=workspace_slug)
       bound_form = AddWorkspace(request.POST, instance=tag)

       if bound_form.is_valid():
           new_tag=bound_form.save()
           return redirect(new_tag)
       return render(request, 'workspaces/ws_edit.html',context={'form':bound_form, 'tag':tag})

   def account_view(request):
       if not request.user.is_authenticated:
           return HttpResponseRedirect(reverse('login'))
       return redirect(request)


def delete(request, id):
    try:
        ws = Workspaces.objects.get(id__iexact=id)
        ws.delete()
        print("Рабочее пространство удалено")
        return render(request, 'workspaces/workspaces.html')
    except:
        print("Workspaces doesn't exists")



class Edit_column(CreateView):
   def get(self, request, id ):
       tag = Columns.objects.get(id__iexact=id)
       bound_form = AddColumn(instance=tag)
       return render(request, 'tasks/edit_column.html', context={'form':bound_form, 'tag':tag})

   def post(self, request, id):
       tag = Columns.objects.get(id__iexact=id)
       bound_form = AddColumn(request.POST, instance=tag)
       if bound_form.is_valid():
           new_tag=bound_form.save()
           return redirect(new_tag)
       return render(request, 'tasks/edit_column.html',context={'form':bound_form, 'tag':tag})

   def account_view(request):
       if not request.user.is_authenticated:
           return HttpResponseRedirect(reverse('login'))
       return redirect(request)
class Edit_task(CreateView):
   def get(self, request, id ):
       tag = Cards.objects.get(id__iexact=id)
       bound_form = AddTask(instance=tag)
       return render(request, 'tasks/edit_task.html', context={'form':bound_form, 'tag':tag})

   def post(self, request, id):
       tag = Cards.objects.get(id__iexact=id)
       bound_form = AddTask(request.POST, instance=tag)
       if bound_form.is_valid():
           new_tag=bound_form.save()
           return redirect(new_tag)
       return render(request, 'tasks/edit_task.html',context={'form':bound_form, 'tag':tag})

   def account_view(request):
       if not request.user.is_authenticated:
           return HttpResponseRedirect(reverse('login'))
       return redirect(request)

class RegisterUser (View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=password)
            send_email_for_verify(request,user)
            return redirect('confirm_email')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)





class LoginUser(LoginView):
    form_class = UserCreationForm
    template_name = "registration/login.html"


    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация'
        return context

    def get_success_url(self):
        return reverse_lazy('workspace')

def logout_user(request):
    logout(request)
    return redirect('home')

class EmailVerify(View):
    def get(self, request, uidb64, token):
        user = self.get_user(uidb64)

        if user is not None and token_generator.check_token(user, token):
            user.email_verify = True
            user.save()
            login(request, user)
            return HttpResponseRedirect('/workspace')
        return HttpResponseRedirect('invalid_verify/')

    @staticmethod
    def get_user(uidb64):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except (
                TypeError,
                ValueError,
                OverflowError,
                User.DoesNotExist,
                ValidationError,
        ):
            user = None
        return user