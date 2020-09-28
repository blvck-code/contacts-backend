from django.urls import path
from contacts.views import ContactList, ContactDetail

urlpatterns = [
    path('', ContactList.as_view()),
    path('<int:id>', ContactDetail.as_view())
]