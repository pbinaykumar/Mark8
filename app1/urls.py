from django.urls import path
from .views import index
from .import views
urlpatterns = [
        path('index',views.index.as_view()),


]