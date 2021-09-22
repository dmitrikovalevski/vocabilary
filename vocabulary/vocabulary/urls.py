"""vocabulary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

# Добавим в urls swagger
from rest_framework import permissions  # Разрешения доступа пользователей
from drf_yasg.views import get_schema_view  # Сама схема swagger
from drf_yasg import openapi  # Описание схемы swagger

# Переменная для схемы
schema_view = get_schema_view(
    # информация схемы
    openapi.Info(
        title="RussianEnglishWord API",
        default_version='v1',
        description='''
        Documentation `ReDoc` [here](/redoc).
      ''',
        contact=openapi.Contact(email="dzmitry.kavaleuski"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# Создадим объект роутера
from rest_framework import routers
# Позовём представления из api.py
from Word.api import RussianWordViewSet, EnglishWordViewSet

# Это пути по которым будем ходить к нашим api представлениям (views)
router = routers.DefaultRouter()
# Регистрация для модели Рус-Англ слов
router.register('russian', RussianWordViewSet)
# Регистрация для модели Англ-Рус слов
router.register('english', EnglishWordViewSet)

urlpatterns = [
    # Путь на моё приложение
    path('', include('Word.urls')),
    # Пути к swagger и документации
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # Путь, который будет указан в браузере
    path('v1/', include(router.urls)),
    # Админка
    path('admin/', admin.site.urls),
]
