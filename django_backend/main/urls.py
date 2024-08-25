from django.urls import path
from main import views

urlpatterns = [
    path('signIn/', views.sign_in_view, name='signIn'),
    path('signUp/', views.sign_up_view, name='signUp'),
]



#notifications
from django.urls import path
from . import views

urlpatterns = [
    path('notifications/', views.get_notifications_view, name='notifications'),
    path('notifications/read/<int:notification_id>/', views.mark_notification_as_read, name='mark_notification_as_read'),
]

