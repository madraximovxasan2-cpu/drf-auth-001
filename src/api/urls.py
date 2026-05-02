from django.urls import path, include

urlpatterns = [
    # path('admin/', include.site.urls),
    path('user/', include("api.users.urls")),
]
        