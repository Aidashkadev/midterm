from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, CreateView
from .models import Contact
from django.urls import reverse_lazy

def contacts_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts/contacts_list.html', {'contacts': contacts})

class ContactDetailView(DetailView):
    model = Contact
    template_name = 'contacts/contacts_detail.html'
    context_object_name = 'contact'

    from django.views.generic.edit import CreateView
from .models import Contact
from django.urls import reverse_lazy

class ContactCreateView(CreateView):
    model = Contact
    fields = ['last_name', 'first_name', 'middle_name', 'phone', 'email', 'photo', 'birth_date']
    template_name = 'contacts/contacts_form.html'
    success_url = reverse_lazy('contacts_list')

# Create your views here.
