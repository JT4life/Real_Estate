from django.urls import path,include
from . import views

urlpatterns = [

    path('',views.index,name='index'),
    path('detail<int:id>',views.detail,name='detail'),
    path('contactAgent<int:id>',views.contactAgent,name='contactAgent'),
    path('search',views.search,name='search'),
    path('getagents',views.getagents,name='getagents'),
    path('houses',views.houses,name='houses',),
    path('buy', views.buy, name='buy', ),
    path('rent', views.rent, name='rent', ),
    path('apartments',views.apartments,name='apartments'),
    path('filtering<str:by>',views.filtering,name='filtering'),
    path('save<str:username><int:id>',views.save_propery,name='save'),
    path('mysaved<str:username>',views.getsaved,name='mysaved'),
    path('remove<str:username><int:id>',views.remove,name='remove'),

]