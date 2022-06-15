from xml.etree.ElementInclude import include
from django.conf import settings
# from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin

from . import views
from .router import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.INDEX, name='home'),
    path('add', views.ADD, name='add'),
    path('edit',views.Edit, name ='edit'),
    path('update/<str:id>', views.Update, name='update'),
    path("delete/<str:id>",views.Delete,name='delete'),
    # -----------------
    path('crud/',include('CRUD.urls'))
]
#