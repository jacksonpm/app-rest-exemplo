from django.conf.urls import url, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework import routers

from app1.views.selecionar_ui import selecionar_ui
from app1.viewset.job_viewset import JobViewSet
from app1.viewset.task_viewset import TaskViewSet

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'jobs', JobViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="REST API - Teste",
        default_version='v1.123abc',
        description="API de Testes",
        terms_of_service="/",
        contact=openapi.Contact(email="jmourajn@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    url(r'^django/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$', selecionar_ui),
]
