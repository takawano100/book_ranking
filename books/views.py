from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

import os
from .models import (
    Books,
)

class BookListView(LoginRequiredMixin, ListView):
    model = Books
    template_name = os.path.join('books', 'book_list.html')

    def get_queryset(self):
        query = super().get_queryset()
        book_title = self.request.GET.get('book_title', None)
        book_author_name = self.request.GET.get('book_author_name', None)
        if book_title:
            query = query.filter(
                title=book_title
            )
        if book_author_name:
            query = query.filter(
                author=book_author_name
            )
        order_by_total = self.request.GET.get('order_by_total', '0')
        if order_by_total == '1':
            query = query.order_by('total_point')
        elif order_by_total == '2':
            query = query.order_by('-total_point')
        return query

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_title'] = self.request.GET.get('book_title', '')
        context['book_author_name'] = self.request.GET.get('book_author_name', '')
        order_by_total = self.request.GET.get('order_by_total', 0)
        if order_by_total == '1':
            context['ascending'] = True
        elif order_by_total == '2':
            context['descending'] = True        
        return context

class BookDetailView(LoginRequiredMixin, DetailView):
    model = Books
    template_name = os.path.join('books', 'book_detail.html')
