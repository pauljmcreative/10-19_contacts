from django.shortcuts import render, get_object_or_404

#  IMPORT CONTACT MODEL
from .models import Contact

# IMPORT LOGIN REQUIRED DECORATOR
from django.contrib.auth.decorators import login_required

@login_required
def contacts_index(request):
  # contacts = Contact.objects.all()
  contacts = Contact.objects.order_by('-last_name').filter(user_id=request.user.id) # to filter contacts we can see when logged in (locks down contacts from logged in people)
  return render(request, 'contacts/contacts_index.html', {'contacts': contacts})

@login_required
def contacts_show(request, contact_id):
  # contact = Contact.objects.get(id=contact_id)
  # contact = Contact.objects.get(id=contact_id, user_id=request.user.id) 
  contact = get_object_or_404(Contact, id=contact_id, user_id=request.user.id) # to make our own 404 page
  return render(request, 'contacts/contacts_show.html', {'contact': contact})



