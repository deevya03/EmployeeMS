
from django.contrib import admin
from django.urls import include, path


from Login import views as login_views
from Register import views as register_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', register_views.home, name="homepage"),
    path('register/', register_views.register, name='registerPage'),
    path('login/', login_views.login, name="loginPage")
]
