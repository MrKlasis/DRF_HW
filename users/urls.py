from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.views.generic import TemplateView
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import RegisterView, ProfileView, activate, RestoreView, main, UserViewSet

app_name = UsersConfig.name


urlpatterns = [
    path('main', main, name='main'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('email_verify/', TemplateView.as_view(template_name='users/verify.html'), name='email_verify'),
    path('activate/<token>', activate, name='activate'),
    path('restore/', RestoreView.as_view(), name='restore'),
]

router = routers.SimpleRouter()
router.register('user', UserViewSet)

urlpatterns += router.urls
