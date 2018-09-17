from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from ideas.forms import IdeaForm
from ideas.models import Idea


class BrainstormView(TemplateView):
    template_name = 'brainstorm.html'

    def get(self, request):
        form = IdeaForm()
        idea = Idea.objects.all().order_by('-created')

        args = {
            'form': form, 'idea': idea
        }
        return render(request, self.template_name, args)

    def idea(self, request):
        form = IdeaForm(request.POST)
        if form.is_valid():
            idea = form.save(commit=False)
            post.user = request.user
            idea.save()

            text = form.cleaned_data['idea']
            form = IdeaForm()
            return redirect('brainstorm:brainstorm')

        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)
