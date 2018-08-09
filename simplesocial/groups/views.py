from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse
from django.views.generic import CreateView, TemplateView, DeleteView, UpdateView, ListView, DetailView, RedirectView
from django.shortcuts import get_object_or_404
from groups.models import Group, GroupMember
from django.contrib import messages
class CreateGroup(LoginRequiredMixin, CreateView):
    fields = ('name', 'description')
    model = Group

class SingleGroup(DetailView):
    model = Group


class ListGroups(ListView):
    model = Group


class JoinGroup(LoginRequiredMixin, RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:single', kwargs={'slug':self.kwargs.get('slug')})

    def get(self, request, *args, **kwargs):
        group = get_object_or_404(Group, slug=self.kwargs.get('slug'))

        try:
            GroupMember.objects.create(user=self.request.user, group=group)
        except IntegrityError:
            messages.warning(self.request, 'Warning Already a Member!')
        else:
            messages.success(self.request, 'You are a now a member!')

        return super().get(request,*args,**kwargs)

class LeaveGroup(LoginRequiredMixin, RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:single', kwargs={'slug':self.kwargs.get('slug')})

    def get(self, request, *args, **kwargs):
        try:
            membership = GroupMember.objects.filter(

                user=self.request.user,
                group__slug = self.kwargs.get('slug')

            ).get()

        except GroupMember.DoesNotExist:
            messages.warning(self.request, 'Sorry you are not in the group')
        else:
            membership.delete()
            messages.success(self.request, 'You have left the group!')
        return super().get(request, *args,**kwargs)
