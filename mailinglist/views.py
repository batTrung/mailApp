from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import MailingList
from .forms import MailingListForm, SubscriberForm
from .mixins import UserCanUseMailingList

class MailingListListView(LoginRequiredMixin, ListView):

	def get_queryset(self):
		return MailingList.objects.filter(owner=self.request.user)

class CreateMailingListView(LoginRequiredMixin, CreateView):
	form_class = MailingListForm
	template_name = 'mailinglist/mailinglist_form.html'

	def get_initial(self):
		return {'owner':self.request.user.id}
		

class DeleteMailingListView(LoginRequiredMixin,UserCanUseMailingList, DeleteView):
	model = MailingList
	success_url = reverse_lazy("mailinglist_list")
	
class MailingListDetailView(LoginRequiredMixin,UserCanUseMailingList, DetailView):
	model = MailingList

class SubscribeToMailingListView(CreateView):
	form_class = SubscriberForm
	template_name = 'mailinglist/subscriber_form.html'

	def get_initial(self):
		return {'mailing_list': self.kwargs["mailinglist_id"]}

	def get_success_url(self):
		return reverse("subscriber_thankyou", kwargs={
			"pk":self.object.mailing_list.id,
		})

class ThankYouForSubscribingView(DetailView):
	model = MailingList
	template_name = "mailinglist/subscription_thankyou.html"

	def get_context_data(self, **kwargs):
		ctx = super().get_context_data(**kwargs)
		mailing_list_id = self.kwargs['mailinglist_id']
		ctx['mailing_list'] = get_object_or_404(MailingList, id=mailing_list_id)

		return ctx