from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from advogado import views
from django.contrib.auth import views as auth_views

router = DefaultRouter()
router.register(r'advogados', views.AdvogadoViewSet)
router.register(r'processos', views.ProcessoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  
    path('', views.register, name='register'), 
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),  
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), 
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', include('advogado.urls')),  
]