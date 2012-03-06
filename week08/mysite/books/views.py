# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse

from books.models import Book
from django.template import Context, loader
from django.http import Http404
from django.template import RequestContext

from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext

