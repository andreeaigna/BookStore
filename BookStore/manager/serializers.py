from rest_framework.serializers import ModelSerializer
from manager.models import Book, Author


# We set the model class on the serializer. This helps the serialize figure out
# how it should represent the data, e.g. dates, numbers or strings.
# It also gets a handle for creating objects in the database.
class BookSerializer(ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'

class AuthorSerializer(ModelSerializer):

    class Meta:
        model = Author
        fields = '__all__'