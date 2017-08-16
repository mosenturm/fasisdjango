# -*- coding: utf-8 -*-

# urls for the core app
# to included in the main urls file

from django.conf.urls import url
from core import views as core_views

urlpatterns = [
    #url(r'^user/(?P<username>[-\w]+)/$', 'marcador.views.bookmark_user',
    #    name='marcador_bookmark_user'),
    #url(r'^$', 'core.views.customer_list', name='core_customer_list'),
    url(r'^customer/edit/(?P<pk>\d+)/$', core_views.customer_edit,
        name='customer_edit'),
    url(r'^customer/delete/(?P<pk>\d+)/$', core_views.customer_delete,
        name='customer_delete'),
    url(r'^customer/create/$', core_views.customer_create,
        name='customer_create'),
    url(r'^ajax/customerlist/$', core_views.get_customers, name='get_customers'), # AJAX
    url(r'^custlist/$', core_views.customer_table, name='customer_table'),
    url(r'^reminder/renew/(?P<pk>\d+)/$', core_views.renew_reminder,
        name='renew_reminder'),
    url(r'^$', core_views.index, name='home'),
]