from django.conf.urls import url, include
from rest_framework import routers
from testapp.api.views import HydJobsCRUDCBV, PuneJobsCRUDCBV, ChennaiJobsCRUDCBV, BloreJobsCRUDCBV, NoidaJobsCRUDCBV, IndoreJobsCRUDCBV
from django.contrib import admin

router = routers.DefaultRouter()
router.register('hydjobsinfo', HydJobsCRUDCBV)
router.register('blorejobsinfo', BloreJobsCRUDCBV)
router.register('punejobsinfo', PuneJobsCRUDCBV)
router.register('chennaijobsinfo', ChennaiJobsCRUDCBV)
router.register('noidajobsinfo', NoidaJobsCRUDCBV)
router.register('indorejobsinfo', IndoreJobsCRUDCBV)

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'', include(router.urls)),
]
