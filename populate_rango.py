import os
os.environ.setdefault(
                        'DJANGO_SETTINGS_MODULE',
                        'tango_with_django_project.settings'
                )

import django
django.setup()

from rango.models import Category, Page

from random import randint

def populate():
    python_pages = [
        {
            'title':'Official Python Tutorial',
            'url':'http://docs.python.org/3/tutorial/',
            'views': randint(1, 35)
        }, {
            'title':'How to Think like a Computer Scientist',
            'url':'http://www.greenteapress.com/thinkpython/',
            'views': randint(1, 35)
        }, {
            'title':'Learn Python in 10 minutes',
            'url':'http://www.korokithakis.net/tutorials/python/',
            'views': randint(1, 35)
        } ]


    django_pages = [
        {
            'title':'Official Django Tutorial',
            'url':'https://docs.djangoproject.com/en/4.0/intro/tutorial101/',
            'views': randint(1, 35)
        }, {
            'title':'Django Rocks',
            'url':'http://www.djangorocks.com/',
            'views': randint(1, 35)
        }, {
            'title':'How to Tango with Django',
            'url':'http://www.tangowithdjango.com/',
            'views': randint(1, 35)
        } ]


    other_pages = [
        {
            'title':'Bottle',
            'url':'http://bottlepy.org/docs/dev/',
            'views': randint(1, 35)
        }, {
            'title':'Flask',
            'url':'http://flask.pocoo.org',
            'views': randint(1, 35)
        } ]


    cats = {
        'Python': {'pages': python_pages},
        'Django': {'pages': django_pages},
        'Other Frameworks': {'pages': other_pages}
    }


    for cat, cat_data in cats.items():
        c = add_cat(cat)

        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'], p['views'])


    update_cat_views_and_likes('Python',128, 64)

    update_cat_views_and_likes('Django',64, 32)

    update_cat_views_and_likes('Other Frameworks',32, 16)

    for c in Category.objects.all():
        print(f'Category: {c}\n\tViews: {c.views}\tLikes: {c.likes}')
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p} views: {p.views}')


def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p


def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c


def update_cat_views_and_likes(object, views, likes):
    o = Category.objects.get(name=object)
    o.views = views
    o.likes = likes
    o.save()


def update_page_views(cat, page, views):
    o = Page.objects.get(category=cat, title=page)
    o.views = views
    o.save()


if __name__ == '__main__':
    print('Starting Rango Population script...')
    populate()
