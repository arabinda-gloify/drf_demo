from django.urls import path
from apiview import views

urlpatterns = [
	path('mobile/', views.MobileListCreateView.as_view()),
	path('mobile/<pk>/', views.MobileRetrieveUpdateDestroy.as_view()),
]
