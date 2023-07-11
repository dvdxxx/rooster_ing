from django.contrib import admin
from django.urls import path
from apps.api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/create-rooster-data/', views.create_rooster_data, name='create_rooster_data'),
]
