from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns=[
    path('',views.fun,name='fun'),
    path('add',views.addition,name='add')
]
urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings)