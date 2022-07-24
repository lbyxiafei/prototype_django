# python manage.py shell < myscript.py
# execfile('myscript.py')

from notes.models import Bookmark, Tag
from django.utils import timezone

bookmark1 = Bookmark(title="Bookmark1", url="www.google.com", pub_date=timezone.now())
bookmark1.save()

print(Bookmark.objects.all())