# python manage.py shell < myscript.py
# exec(open('myscript.py').read())

from notes.models import Bookmark, Tag
from django.utils import timezone

b1 = Bookmark(title="Bookmark1", url="www.google.com", pub_date=timezone.now())
b1.save()

t1,t2 = Tag(name="algo"),Tag(name="cheatsheet")
t1.save()
t2.save()

b1.tag.add(t1,t2)

print(Bookmark.objects.all())