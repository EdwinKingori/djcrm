from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect

# restricting the agent from viewing the leads usinga customized mixin


class OrganizerLoginRequiredMixin(AccessMixin):
    """Verify that the current user is authenticated and is an organizer."""

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_organizer:
            return redirect("index")
        return super().dispatch(request, *args, **kwargs)
