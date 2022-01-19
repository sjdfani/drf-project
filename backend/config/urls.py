from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from AppApi.views import RevokeToken

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('blog/', include('blog.urls')),
    path('api/', include('AppApi.urls')),
    path('api/token-auth/', obtain_auth_token),
    path('api/revoke-token/', RevokeToken.as_view()),
]
