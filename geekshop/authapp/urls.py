
from django.urls import path
from authapp.views import RegisterListView, LoginListView, Logout, ProfileFormView

app_name = 'authapp'
urlpatterns = [
    path('register/', RegisterListView.as_view(), name='register'),
    path('login/', LoginListView.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('profile/', ProfileFormView.as_view(), name='profile'),
    path('verify<str:email>/<str:activate_key>/', RegisterListView.verify, name='verify'),
]



