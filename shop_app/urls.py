from django.urls import path
from shop_app.views import *


urlpatterns = [

    path('', index, name='index'),
    path('display_laptops', display_laptops, name='display_laptops'),
    path('display_desktops', display_desktops, name='display_desktops'),
    path('display_mobiles', display_mobiles, name='display_mobiles'),

    path('add_laptop', add_laptop, name='add_laptop'),
    path('add_desktop', add_desktop, name='add_desktop'),
    path('add_mobile', add_mobile, name='add_mobile'),

    path('edit_laptop/<int:id>', edit_laptop, name='edit_laptop'),
    path('edit_desktop/<int:id>', edit_desktop, name='edit_desktop'),
    path('edit_mobile/<int:id>', edit_mobile, name='edit_mobile'),

    path('delete_mobile/(?P<pk>\d+)/$', delete_laptop, name='delete_laptop'),
    path('delete_desktop/(?P<pk>\d+)/$', delete_desktop, name='delete_desktop'),
    path('delete_laptop/(?P<pk>\d+)/$', delete_mobile, name='delete_mobile'),
]
