from django.shortcuts import render
from django.views import View
from contact_us.models import ContactUs


class ContactUsView(View):

    def get(self, request, *args, **kwargs):
        return render(request, "index.html")

    def post(self, request, *args, **kwargs):

        obj = ContactUs.objects.create(name=request.POST['name'],
                                       phone_number=request.POST['phone_number'],
                                       email=request.POST['email'],
                                       message=request.POST['message'])

        return render(request, 'index.html')
