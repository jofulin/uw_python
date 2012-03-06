from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView
from books.models import Book

urlpatterns = patterns('',
    url(r'^$',
        ListView.as_view(
            queryset=Book.objects.order_by('-title')[:5],
            context_object_name='latest_book_list',
            template_name='books/index.html')),
    url(r'^(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Book,
            template_name='books/detail.html')),
    url(r'^(?P<pk>\d+)/results/$',
        DetailView.as_view(
            model=Book,
            template_name='books/results.html'),
        name='book_results'),

)
