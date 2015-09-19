ANN: Django Better Cache 0.5 Released
#####################################
:date: 2012-01-22 19:55
:author: Calvin Spealman (noreply@blogger.com)
:category: technology
:tags: bettercache, django, python, announcement
:slug: ann-django-better-cache-05-released

I am announcing the release of Django Better Cache 0.5 today. This
release includes a move to sphinx as a documentation tool and a new
component, the bettercache.objects module, which provides a lite
ORM-like interface for caching data.

Please read the full, but short documentation `over at Read The
Docs <http://readthedocs.org/docs/django-better-cache/en/latest/>`__ for
details on the bettercache {% cache %}tag and the bettercache.objects
ORM, and have a much easier time with your caching needs.

Here is just a quick example of the new cache models, from the docs:

.. code-block:: python

    class User(CacheModel):
        username = Key()
        email = Field()
        full_name = Field()

    user = User(
        username = 'bob',
        email = 'bob@hotmail.com',
        full_name = 'Bob T Fredrick',
    )
    user.save()

    ...

    user = User.get(username='bob')
    user.email == 'bob@hotmail.com'
    user.full_name == 'Bob T Fredrick'
