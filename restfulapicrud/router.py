from taskmanage.viewsets import TasksmViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('taskmanage',TasksmViewset)

