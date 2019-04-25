from django.core.exceptions import PermissionDenied, FieldDoesNotExist
from .models import MailingList


class UserCanUseMailingList:
	def get_object(self, queryset=None):
		obj = super().get_object(queryset)
		user = self.request.user
		if isinstance(obj, MailingList):
			if obj.user_can_use_mailing_list(user):
				return obj
			else:
				raise PermissionDenied()
		