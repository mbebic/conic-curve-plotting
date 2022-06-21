from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('conicgraph', views.conicgraph, name='conicgraph'),
    path('library', views.library, name='library'),
    # path("curveplotdata/<int:curve_id>", views.curveplotdata, name="curveplotdata")
]