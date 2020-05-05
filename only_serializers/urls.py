from django.urls import path
from only_serializers import views 

urlpatterns = [
	path('players/', views.PlayersListView.as_view()),
	path('players/<pk>/', views.PlayersRetriveUpdateDestroy.as_view()),
]
