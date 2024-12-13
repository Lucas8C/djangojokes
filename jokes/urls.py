from django.urls import path
from .views import JokeDetailView, JokeListView

app_name = 'jokes'

urlpatterns = [
    path('', JokeListView.as_view(), name='joke_list'),
    path('<int:pk>/', JokeDetailView.as_view(), name='joke_detail'),
]
