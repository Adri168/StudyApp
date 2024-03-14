""" User's views """

# Django
from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from django.contrib.auth import views as auth_views
from django.urls import reverse, reverse_lazy

# Forms
from users.forms import SignupForm

# Models
from users.models import Maestro

# External lib

# Create your views here.
class Selection(TemplateView):
    """ Selection of type profile view
    
    ex: the teacher would select the teacher option
    """
    template_name = "users/login.html"

class SignupTeacherView(FormView):
    """ Signup view for teacher type user """
    template_name = "users/teacherSignup.html"
    form_class = SignupForm
    success_url = reverse_lazy('users:select')

    def form_valid(self, form):
        """Save form data."""
        form.save(Maestro)
        return super().form_valid(form)
