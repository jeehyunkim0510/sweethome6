from django.urls import path

from profileapp.views import ProfileCreateView, ProfileUpdateView, ProfileDetailView, ProfileDeleteView

app_name='profileapp'


# urlpatterns =[
#     path('create/', ProfileCreateView.as_view(), name='create'),
#     path('detail/<int:pk>/', ProfileDetailView.as_view(), name='detail'),
#     path('delete/', ProfileDeleteView.as_view(), name='delete'),
#     path('update/', ProfileUpdateView.as_view(), name='update'),
#     path('list/', ProfileListView.as_view(), name='list'),
# ]

urlpatterns = [
    path('create/', ProfileCreateView.as_view(), name='create'),

    # user_id로 접근하는 URL 패턴 추가
    path('detail/user<int:user_id>/', ProfileDetailView.as_view(), name='detail_by_user'),
    path('delete/user<int:user_id>/', ProfileDeleteView.as_view(), name='delete_by_user'),
    path('update/user<int:user_id>/', ProfileUpdateView.as_view(), name='update_by_user'),
]

# path('detail/<int:pk>/', ProfileDetailView.as_view(), name='detail'),
# path('delete/<int:pk>/', ProfileDeleteView.as_view(), name='delete'),
# path('update/<int:pk>/', ProfileUpdateView.as_view(), name='update'),