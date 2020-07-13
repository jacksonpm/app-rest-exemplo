from django.conf.urls import url, include
from rest_framework import routers

# Routers provide an easy way of automatically determining the URL conf.
from app1.viewset.job_viewset import JobViewSet
from app1.viewset.task_viewset import TaskViewSet

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'jobs', JobViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
