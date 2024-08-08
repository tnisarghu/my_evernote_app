import algoliasearch_django as algoliasearch
from notes.models import Note

algoliasearch.register(Note)