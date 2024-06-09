from django.urls import path, include
from auth_options.views import GitHubLogin, GoogleLogin

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('registration/', include('dj_rest_auth.registration.urls')),
    path('github/login/', GitHubLogin.as_view(), name='github_login'),
    path('google/login/', GoogleLogin.as_view(), name='google_login'),
]