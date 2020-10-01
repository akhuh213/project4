
from .models import Post
import django_filters

class SearchFilter(django_filters.FilterSet):
    class Meta:
        model = Post
        fields = ['title', 'category', 'age', 'zipcode']