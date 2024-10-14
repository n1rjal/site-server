from django.urls import path
from . import views

urlpatterns = [
    path(
        "",
        views.NewsletterCreateView.as_view(),
        name="newsletter-create",
    ),
]
