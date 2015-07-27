# -*- coding: utf-8 -*-
from models import Contact
from django import forms
from django.contrib import messages
from django.views.generic.edit import CreateView
from django.core.mail import mail_admins


#  creating forms
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        help_texts = {'name': u'Имя отправителя', 'subject': u'Тема письма', 'email': u'email отправителя'}
        fields = '__all__'


# create Views
class ContactCreateView(CreateView):
    model = Contact
    form_class = ContactForm
    success_url = '/contact/'

    def get_context_data(self, **kwargs):
        context = super(ContactCreateView, self).get_context_data(**kwargs)
        context['page_title'] = 'Написать автору сайта'
        return context

    def form_valid(self, form):
        form = super(ContactCreateView, self).form_valid(form)
        name = self.object.contact_name
        subject = self.object.contact_subject
        message = self.object.contact_text
        email = self.object.contact_email
        date = self.object.contact_date
        mail_admins(subject, message, fail_silently=False, connection=None, html_message=None)
        messages.success(self.request, 'Mail from %s successfully send' % name)
        return form
