from django.shortcuts import render

#  IMPORT CONTACT MODEL
from .models import Contact

# IMPORT LOGIN REQUIRED DECORATOR
from django.contrib.auth.decorators import login_required

@login_required
def contacts_index(request):
  contacts = Contact.objects.all()
  return render(request, 'contacts/contacts_index.html', {'contacts': contacts})

@login_required
def contacts_show(request, contact_id):
  contact = Contact.objects.get(id=contact_id)
  return render(request, 'contacts/contacts_show.html', {'contact': contact})



