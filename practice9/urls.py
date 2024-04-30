from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

route = DefaultRouter()
route.register('student',views.StudentApi,basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls)),
    path('gettoken/', obtain_auth_token),

]
