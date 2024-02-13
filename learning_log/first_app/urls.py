"""first_app için URL örüntülerini tanımlar."""
from django.urls import path
from .import views
app_name = 'first_app'

urlpatterns = [
    # Home page
    path('',views.index,name = 'index'),
    #Bütün konuları gösteren sayfa.
    path('topics/',views.topics,name='topics'),
    #Tek bir konu için ayrıntı sayfası.
    path('topics/<int:topic_id>/',views.topic,name='topic'),
    #Yeni konu eklemek için olan sayfa.
    path('new_topic/',views.new_topic,name='new_topic'),
    #Yeni bir girdi eklemek için olan sayfa.
    path('new_entry/<int:topic_id>/',views.new_entry,name='new_entry'),
    #Bir girdiyi düzenlemek için olan sayfa.
    path('edit_entry/<int:entry_id>/',views.edit_entry,name='edit_entry'),
]


