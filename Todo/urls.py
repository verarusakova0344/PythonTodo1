from django.urls import path, include
from django.views.decorators.cache import cache_page
from django.views.generic import TemplateView

from Todo.views import *

urlpatterns =[
    path('', index, name='home'),
    path('lk/', lk, name='lk'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', MyLoginView.as_view(), name='login'),
    path('task/<slug:workspace_slug>/', TaskHome.as_view(), name='task'),
    path('task/<slug:workspace_slug>/need_do', TaskHomeNeed.as_view(), name='task_need_do'),
    path('task/<slug:workspace_slug>/is_do', TaskHomeIs.as_view(), name='task_is_do'),
    path('task/<slug:workspace_slug>/timeout', TaskHomeTime.as_view(), name='task_timeout'),
    path('add_workspace/', Add_ws.as_view(), name="add_workspace"),
    path('add_access/', Add_access.as_view(), name="add_access"),
    path('update_workspace/<slug:workspace_slug>/', Edit_ws.as_view(), name="update_workspace"),
    path('workspace/', WorkspaceHome.as_view(), name='workspace'),
    path('delete/<int:id>/', delete,  name='delete'),
    path('update_column/<int:id>/', Edit_column.as_view(), name="update_column"),
    path('update_task/<int:id>/', Edit_task.as_view(), name="update_task"),
    path('add_column/<slug:workspace_slug>/', Add_column.as_view(), name="add_column"),
    path('add_task/<slug:workspace_slug>/', Add_task.as_view(), name="add_task"),
    path('', include('django.contrib.auth.urls')),
    path('confirm_email/', TemplateView.as_view(template_name='registration/confirm_email.html'), name='confirm_email'),
    path('<uidb64>/<token>/', EmailVerify.as_view(), name='verify_email'),
    path('invalid_verify/', TemplateView.as_view(template_name='registration/invalid_verify.html'),
         name='invalid_verify'),
]

