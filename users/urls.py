from django.urls import path
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet, RegisterView, ProfileView, RestoreView, MainView, ActivateView

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('main/', MainView.as_view(), name='main'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('restore/', RestoreView.as_view(), name='restore'),
    path('activate/<token>/', ActivateView.as_view(), name='activate'),
]

urlpatterns += router.urls
