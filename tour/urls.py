from django.urls import path
from .views import CarList, CarRetrieve, TourList, TourRetrieve, BookingDelete, BookingCreate, BookingUpdate, CreateReview, DeleteReview


urlpatterns = [
    path('car_list/', CarList.as_view()),
    path('car_retrieve/<int:pk>/', CarRetrieve.as_view()),
    path('tour_list/', TourList.as_view()),
    path('tour/<int:pk>/', TourRetrieve.as_view()),
    path('booking_create/', BookingCreate.as_view()),
    path('booking_delete/<int:pk>/', BookingDelete.as_view()),
    path('booking_update/<int:pk>/', BookingUpdate.as_view()),
    path('review_create/', CreateReview.as_view()),
    path('review_delete/', DeleteReview.as_view())
]

