from django.urls import path

from staff.views import settings

app_name = 'staff'
urlpatterns = [
     path('', settings.index, name='index'),
     path('packages/', settings.membership_packages, name='membership_packages'),
     path('helptexts/', settings.helptexts, name='helptexts'),
     path('motd/', settings.motd, name='motd'),
     path('edit_rooms/', settings.edit_rooms, name='edit_rooms'),
     #path('doc_upload/', settings.document_upload, name='doc_upload'),
]

# Copyright 2019 Office Nomads LLC (https://officenomads.com/) Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at https://opensource.org/licenses/Apache-2.0 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
