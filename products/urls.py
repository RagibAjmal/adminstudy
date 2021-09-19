from django.urls import path,include
from django.urls.resolvers import URLPattern

from products import views

urlpatterns=[
    path('latest-products/',views.LatestEventsList.as_view()),
    path('events/<slug:category_slug>/<slug:product_slug>/',views.EventDetail.as_view()),
   ]