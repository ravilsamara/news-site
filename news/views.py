from django.shortcuts import render, redirect
from .models import Articles
from .form import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView


def news_home(request):
    news = Articles.objects.order_by('-date')
    data = {'news': news}
    return render(request, 'news/news_home.html', data)


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'
    form = ArticlesForm()
    data = {'form': form, 'error': error}
    return render(request, 'news/create.html', data)


class NewDetailsView(DetailView):
    model = Articles
    template_name = 'news/detail_view.html'
    context_object_name = 'article'


class NewsUpdateViews(UpdateView):
    model = Articles
    template_name = 'news/create.html'
    form_class = ArticlesForm


class NewsDeleteViews(DeleteView):
    model = Articles
    success_url = '/news/'
    template_name = 'news/news_delete.html'
