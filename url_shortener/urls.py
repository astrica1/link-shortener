from django.urls import path
from . import views

urlpatterns = [
    path('<str:short_url>', views.RedirectToLongUrl.as_view(), name='url.redirect'),
]