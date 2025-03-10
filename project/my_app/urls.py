"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

from .views import update_mou_view

urlpatterns = [
    path('mou/update/<int:id>/', update_mou_view, name='update_mou'),

    path('', views.login_view, name='login'),  # Set login as the first page
    path('create-mou/', views.create_mou_view, name='create_mou'),  # Create MoU page
    path('index/', views.index_view, name='index'),  # Add index URL
    path('view-mou/', views.view_mou_view, name='view_mou'),  # View MoU page
    path('edit_mou/<int:id>/', views.edit_mou_view, name='edit_mou'),
    path('delete_mou/<int:id>/', views.delete_mou_view, name='delete_mou'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
