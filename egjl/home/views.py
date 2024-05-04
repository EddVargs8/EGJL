from django.shortcuts import render
from django.views import generic
from django.contrib.auth.models import User
from home import models

# Create your views here.

class Index(generic.View):
    template_name = "index.html"

    usuarios = User.objects.all()

    def get(self, request):
        context = {"usuarios": self.usuarios}
        return render(request, self.template_name, context)

class About(generic.View):
    template_name = "about.html"
    context = {}

    def get(self, request):
        self.context = {
            "usuarios": models.User.objects.all(),
        }
        return render(request, self.template_name, self.context)

class DetailUser(generic.View):
    template_name = "detail_user.html"
    context = {}

    def get(self, request, pk):
        self.context = {
            "user_detail": models.User.objects.get(pk=pk),
        }
        return render(request, self.template_name, self.context)
