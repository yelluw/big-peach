import logging
from uuid import uuid4
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.contrib.auth.models import User
from members.forms import MemberForm
from members.models import Member


logger = logging.getLogger(__name__)


class IndexView(FormView):
    form_class = MemberForm
    template_name = 'index.html'
    success_url = reverse_lazy('index')
    
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        # show hide membership form
        context['is_member'] = self.request.session.get('is_member', False) 
        return context

    def form_valid(self, form):
        user = User.objects.create(
            email=form.cleaned_data['email'],
            username=uuid4().hex
        )
        Member.objects.create(
            user=user
        )
        self.request.session['is_member'] = True
        return super().form_valid(form)
