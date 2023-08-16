from django.urls import path
from Todo import views

urlpatterns = [
    path('Data',views.UserProfileView.as_view(),name='registration'),
    path('Data/<int:id>', views.UserProfileEditView.as_view(),name='edit'),
    path('',views.TaskView.as_view(), name='taskview'),
    path('task/<int:id>',views.TaskDetails.as_view(), name='taskDetails'),
]
