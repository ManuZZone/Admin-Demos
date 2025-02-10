from django.contrib import admin
from django.views.generic import TemplateView
from unfold.admin import ModelAdmin
from unfold.views import UnfoldModelAdminViewMixin
from .models import Payment
from django.urls import path


class PaymentBasedView(UnfoldModelAdminViewMixin, TemplateView):
    title = "Custom Title"  # required: custom page header title
    permission_required = () # required: tuple of permissions
    template_name = "payments/index.html"
    

@admin.register(Payment)
class PaymentAdmin(ModelAdmin):
    def get_urls(self):
        return super().get_urls() + [
            path(
                "payments",
                PaymentBasedView.as_view(model_admin=self),  # IMPORTANT: model_admin is required
                name="payment"
            ),
        ]
    