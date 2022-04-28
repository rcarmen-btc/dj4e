from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import path, reverse_lazy, reverse
from django.views import View

from ads.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView
from ads.models import Ad, Comment
from ads.forms import CreateForm


class AdListView(OwnerListView):
    model = Ad
    # By convention:
    # template_name = "myarts/ad_list.html"


class CommentCreateView(LoginRequiredMixin, View):

    def post(self, request, pk) :
        f = get_object_or_404(Ad, id=pk)
        comment = Comment(text=request.POST['comment'], owner=request.user, forum=f)
        comment.save()
        return redirect(reverse('forums:forum_detail', args=[pk]))


class CommentDeleteView(OwnerDeleteView):
    model = Comment
    template_name = "forums/comment_delete.html"


class AdDetailView(OwnerDetailView):

    model = Ad

    def get_context_data(self, **kwargs):
        comments = Comment.objects.filter(ad=kwargs['object']).order_by('-updated_at')
        context = super().get_context_data(**kwargs)
        context['comments'] = comments
        return context


class AdCreateView(OwnerCreateView):
    model = Ad
    # List the fields to copy from the Article model to the Article form
    template_name = 'ads/ad_form.html'
    fields = ['title', 'text', 'price']
    success_url = reverse_lazy('ads:all')

    def get(self, request, pk=None):
        form = CreateForm()
        ctx = {
            'form': form,
        }
        return render(request, self.template_name, ctx)

    def post(self, request, pk=None):
        form = CreateForm(request.POST, request.FILES or None)

        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)

        # Add owner to the model before saving
        pic = form.save(commit=False)
        pic.owner = self.request.user
        pic.save()
        return redirect(self.success_url)


class AdUpdateView(OwnerUpdateView):
    model = Ad
    fields = ['title', 'text']
    # This would make more sense
    # fields_exclude = ['owner', 'created_at', 'updated_at']


class AdDeleteView(OwnerDeleteView):
    model = Ad


def stream_file(request, pk):
    pic = get_object_or_404(Ad, id=pk)
    response = HttpResponse()
    response['Content-Type'] = pic.content_type
    response['Content-Length'] = len(pic.picture)
    response.write(pic.picture)
    return response
