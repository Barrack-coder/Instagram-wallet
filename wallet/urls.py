from django.conf import settings
from django.conf.urls.static import static
from django.urls import path                                                                                             
from .views import(
     PostListView
)
from wallet import views
# from photos import views

urlpatterns = [
     
     path('index', views.index, name='index'),
     path('', views.signin, name='signin'),
     path('register', views.register, name='register'),
     path('account', views.profile, name='profile'),
     path('post_list',PostListView.as_view(), name='post_list'),   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)