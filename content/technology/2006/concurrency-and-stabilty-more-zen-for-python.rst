Concurrency and Stabilty. More Zen for Python.
##############################################
:date: 2006-09-19 07:10
:author: Calvin Spealman (noreply@blogger.com)
:tags: python, programming
:slug: concurrency-and-stabilty-more-zen-for-python
:status: published
:category: technology


|image0|

I was planning on writing something about the current
conversations on the Python-3000 list about concurrency, which just
doesn't stop being brought up and never gets resolved to any point that
anyone is happy with. In an unrelated action, I went to check on my
older blog, which I thought of resurrecting for some non-development
articles, and I found a draft from a previous time the topic came up. I
read it and was surprised to find that it proposes pretty much exactly
what is being put on the table over this past weekend, with reference to
walling off multiple interpreters in a single process and controlling
messages past between them. The same technique scales for multiple
cores, multiple processors, or multiple machines.

I've decided to take the easy way out and just post the original draft
with minor editing. I enjoy how spot on I ended up being with what is
currently becomming an acceptable solution, it might seem. The original
was written nearly a year ago. Does this mean my predictions are worth
something? Decide for yourself!

Concurrency is a hot topic on the Python mailing lists lately. There
is a strong push to get some kind of native concurrency into Python, as
the 3.0 branch is a great opportunity to do things that we can't
otherwise do, as they would break old code. If we don't get something in
now, particularly, something that can scale to hundreds of thousands of
tasks and take advantage of multiple processors, we may not get a chance
at what could be the best improvement of the language, until the next
major version 4.0.

A large part of the problems stems from how horrible an idea threads
really are, as they are typically implemented. Threads, as the basic
level, are just multiple pre-emptive tasks running with access to the
same memory space. Doing this can be a boost for performance, but is
hell to control properly. The threads must be syncronized to access
their shared resources without clobbering each other. This can be done,
but it is very error prone and very difficult to debug.

The solutions seem to lean toward two ends of the spectrum: cooperative
tasks and processes. With cooperative tasks, each concurrent unit runs
until it says "OK, I'll let someone else run now", and so there is no
explicit syncronization needed, because nothing happens without you
knowing it, idealy.

Processes, on the other hand, are basically threads without shared
memory. These are the same way the concept of processes are implemted at
an OS level. Some, including Guido van Russom, even think that is how we
should go: multiple system processes communicating via pipes and
sockets.

What I propose is a process implementation with python itself. This
would offer a lightweight process execution, where each process would
consist of a thread of execution and an "object space". Each thread
would only be able to access objects within this space. Communication
would occure through channels between processes, which can be used like
generators (gen.send(10), for example). I've created a basic
implemenation, available on my webserver, here.

With my basic demo, you can create object spaces, each with their own
global and local dictionaries. There is no real protection, but it shows
how it would work and offers an idea of how it would be used if we had
real protected object spaces. You can run a function in a space with the
run method, which takes a resonse function first, which is called when
the the function returns and will be passed the called functions return
value. If a function is already executing, the request is queued until
its turn.

I need to look around and find that demo/prototype code. I barely
remember writing it, but I remember being pleased with the results. I'll
look around and resurrect it. Perhaps it will serve as an interesting
proof of concept for a possible solution to some of our concurrency
problems. I wish I could put more work into a solution now, but at the
moment I have little practicle use for concurrency of this type. Maybe
in a while I can find justification to spend time on it.

.. |image0| image:: /images/cailloux.jpg
