from rest_framework import routers
from rest_framework.routers import DefaultRouter

from CRUD.views import EmployeeViewSet, SameenViewSet

router: DefaultRouter = routers.DefaultRouter()
router.register('Employee', EmployeeViewSet)
router.register('sameen', SameenViewSet)