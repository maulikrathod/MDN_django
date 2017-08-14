from django.shortcuts import render
from .models import Author, Book, BookInstance, Genre
from django.views import generic


# Create your views here.
def index(request):
    """  View function for home page of site.    """
    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    # Available Books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count() # the 'all()' is implied by default

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context={'num_books':num_books, 'num_instances':num_instances, 'num_authors':num_authors, 'num_instances_available':num_instances_available, 'num_visits':num_visits})


# Class Based View
class BookListView(generic.ListView):
    model = Book
    paginate_by = 5

    # context_object_name = 'my_book_list' # your own name for the list as a template variable
    # queryset = Book.objects.filter(title_icontains='war')[:5] # Get 5 books containing the title war
    # template_name = 'books/my_arbitrary_template_name_list.html'    # Specify your own template name/location

    # def get_queryset(self):
    #     return Book.objects.filter(title_icontains='war')[:5] # Get 5 books containing the title war

    # def get_context_data(self, **kwargs):
    #     # call the base implementation first to get a context
    #     context = super(BookListView, self).get_context_data(**kwargs)
    #     # get blog from id and add it to the context
    #     context['some-data'] = 'This is some data'
    #     return context

class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author

class AuthorDetailView(generic.DetailView):
    model = Author
