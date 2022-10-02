from django.urls import path
from . import views
from rest_framework import routers

app_name = "chat"

router = routers.SimpleRouter()

router.register("", views.OrganizationViewSet)

urlpatterns = router.urls
