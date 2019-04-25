from django.urls import path
from . import views

urlpatterns = [
	path('', views.MailingListListView.as_view(), name='mailinglist_list'),
	path('new/', views.CreateMailingListView.as_view(), name='create_mailinglist'),
	path('<uuid:pk>/delete/', views.DeleteMailingListView.as_view(), name="delete_mailinglist"),
	path('<uuid:pk>/manage/', views.MailingListDetailView.as_view(), name="manage_mailinglist"),

	path("<uuid:mailinglist_id>/subscribe/", views.SubscribeToMailingListView, name="subscribe"),
	path("<uuid:pk>/thankyou/", views.ThankYouForSubscribingView, name="subscriber_thankyou"),
]