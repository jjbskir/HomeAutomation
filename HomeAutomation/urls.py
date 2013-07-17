from django.conf.urls import patterns, url
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from HomeAutomation import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'homeautomation', views.LampViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browseable API.
urlpatterns = patterns('',
    url(r'^', include(router.urls)),
)