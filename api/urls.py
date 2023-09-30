from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter

# Creating Routing Object
router = DefaultRouter()

# Register ViewSet with Router
router.register('bank-list', views.BankViewSet) #url to show lists of bank
router.register('branch-list', views.BranchViewSet) #url to show list of branch 
router.register('banklist-with-branches', views.Bank_with_BranchesViewSet) #url to show bank with their branches

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls',namespace='rest_framework')),
]
