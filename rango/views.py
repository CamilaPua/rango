from rango.models import Category, Page
from rango.forms import CategoryForm, PageForm
from django.shortcuts import render, redirect
from django.urls import reverse

def index(request):
    context_dict = {
        'aboldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'
    }
    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]
    context_dict['categories'] = category_list
    context_dict['pages'] = page_list
    return render(request, 'rango/index.html', context=context_dict)

def show_category(request, category_name_slug):
    context_dictionary = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dictionary['pages'] = pages
        context_dictionary['category'] = category
    except Category.DoesNotExist:
        context_dictionary['category'] = None
        context_dictionary['pages'] = None
    return render(request, 'rango/category.html', context=context_dictionary)

def about(request):
    return render(request, 'rango/about.html')

def add_category(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/')
        else:
            print(form.errors)
    return render(request, 'rango/add_category.html', {'form': form})

def add_page(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category = None
    if category is None:
        return redirect(reverse('rango:index'))
    form = PageForm()
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if category:
                page = form.save(commit=False)
                page.category = category
                page.views = 0
                page.save()
                return redirect(reverse('rango:show_category',
                                         kwargs={'category_name_slug':
                                                 category_name_slug}))
        else:
            print(form.errors)
    context_dict = {'form': form, 'category': category}
    return render(request, 'rango/add_page.html', context=context_dict)
