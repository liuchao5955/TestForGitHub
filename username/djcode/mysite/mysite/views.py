from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse,Http404
from django.shortcuts import render_to_response
from books.models import Book,Author
import datetime
from django.utils import simplejson

def hello(request):
    return HttpResponse("Hello world")

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)

def current_datetime(request):
    now = datetime.datetime.now()
    return render_to_response('current_datetime.html',{'current_date':now})

def rq(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))

def search_form(request):
    return render_to_response('search_form.html')

def search(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        elif len(q) > 20:
            error = True
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('search_results.html',
                {'books': books, 'query': q})
    return render_to_response('search_form.html',
        {'error': error})

def insert_Author(request,lastname):
    author = Author(last_name = lastname,first_name = 'liu',email = 'liuchao5955@163.com')
    author.save()
    ret = {
            "result": True,
            }
    return HttpResponse(simplejson.dumps(ret), mimetype="application/json")

def getPostData(request):
    print request.POST
    print request.FILES
    if "name" in request.POST:
        lastname = request.POST['name']
    else:
        lastname = ""
    author = Author(last_name = lastname,first_name = 'liu',email = 'liuchao5955@163.com')
    author.save()
    ret = {
            "result": True,
            }
    return HttpResponse(simplejson.dumps(ret), mimetype="application/json")
