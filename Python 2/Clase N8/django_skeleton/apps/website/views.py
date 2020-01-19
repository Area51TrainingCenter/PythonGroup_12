# coding:utf-8
from django.views.generic import TemplateView
from blog.models import Category, Post, Footer, FooterSocialNet, Tag, Comments
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.forms import ContactForm
from django.http import HttpResponseRedirect
import urllib.request, json
from django.http import JsonResponse

from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.shortcuts import redirect

from core.form import GenerateRandomUserForm
from core.task import create_random_user_accounts
from django.shortcuts import render


class UsersListView(ListView):
    template_name = 'users_list.html'
    model = User


class RedisView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'redis.html', context=None)


class GenerateUsers(FormView):
    template_name = 'generateuser.html'
    form_class = GenerateRandomUserForm

    def form_valid(self, form):
        total = form.cleaned_data.get('total')
        create_random_user_accounts(total)
        messages.success(self.request, 'Estamos generando los usuario refresca la web en unos momentos')
        return HttpResponseRedirect('./')


class Home(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['category'] = Category.objects.all()
        posts = Post.objects.all()
        page = self.request.GET.get('page', 1)
        paginator = Paginator(posts, 4)
        try:
            context['publication'] = paginator.page(page)
        except PageNotAnInteger:
            context['publication'] = paginator.page(1)
        except EmptyPage:
            context['publication'] = paginator.page(paginator.num_pages)
        context['publication_all'] = posts

        footer = Footer.objects.get(id=1)
        context['footer'] = footer
        context['footernet'] = footer.footersocialnet_set.filter().order_by('id')
        context['footernet_2'] = FooterSocialNet.objects.filter(category=footer.id)

        lista_categoria = []

        with urllib.request.urlopen('http://localhost:8000/category/') as url:

            context['category'] = json.loads(url.read().decode())
            #for i in data:

            #    lista_categoria(i)

        return context


class Publication(TemplateView):
    template_name = 'single-standard.html'

    def post(self, request, *args, **kwargs):
        Comments.objects.create(
            name=request.POST.get('cName'),
            email=request.POST.get('cEmail'),
            website=request.POST.get('cWebsite'),
            message=request.POST.get('cMessage'),
        )
        return HttpResponseRedirect('./')

    def get(self, request, *args, **kwargs):
        fort = ContactForm
        return (self.render_to_response(
            self.get_context_data(kwargs=kwargs, form=fort)))

    def get_context_data(self, **kwargs):
        context = super(Publication, self).get_context_data()

        context['post'] = Post.objects.filter(id=kwargs['kwargs']['id']).get()
        context['prev'] = (Post.objects.filter(id=int(kwargs['kwargs']['id'])-1).get()
                           if Post.objects.filter(id=int(kwargs['kwargs']['id'])-1).exists() else '')
        context['nextp'] = (Post.objects.filter(id=int(kwargs['kwargs']['id'])+1).get()
                           if Post.objects.filter(id=int(kwargs['kwargs']['id'])+1).exists() else '')
        context['tag'] = Post.tag.through.objects.filter()
        context['comments'] = Comments.objects.filter(post_id=kwargs['kwargs']['id'])
        context['comments_count'] = len(context['comments'])
        #with urllib.request.urlopen('http://localhost:5000/service_userdjango') as url:
        #    data = json.loads(url.read().decode())
        #    context['descrition'] = (data['userdjango'][0]['description'])
        #    context['name'] = (data['userdjango'][0]['name'])

        return context


class Test(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context


class ServiceCategory(TemplateView):

    def get(self, request, *args, **kwargs):
        category = Category.objects.all()
        response = [{'name': b.name,
                     'id': b.id

        }for b in category]
        return JsonResponse(response, safe=False)



