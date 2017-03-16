from django.conf.urls import url
from .views import profile, logout, login, register

urlpatterns = [
    url(r'^profile$', profile, name='profile'),
    url(r'^logout$', logout, name='logout'),
    url(r'^login$', login, name='login'),
    url(r'^register$', register, name='register'),
]