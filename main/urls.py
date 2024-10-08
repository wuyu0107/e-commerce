from django.urls import path
from main.views import show_main, create_note_entry, show_xml, show_json, show_json_by_id, show_xml_by_id, register, login_user, logout_user, edit_entry, delete_entry, add_note_entry_ajax

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-note-entry', create_note_entry, name='create_note_entry'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name="show_json"),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit-entry/<uuid:id>', edit_entry, name='edit_entry'),
    path('delete/<uuid:id>', delete_entry, name='delete_entry'),
    path('create-note-entry-ajax', add_note_entry_ajax, name='add_note_entry_ajax')
]