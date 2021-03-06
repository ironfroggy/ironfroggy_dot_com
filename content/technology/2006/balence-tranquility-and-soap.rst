Balance, Tranquility, and SOAP
##############################
:date: 2006-10-11 06:33
:author: Calvin Spealman (noreply@blogger.com)
:tags: programming, development
:slug: balance-tranquility-and-soap
:category: technology

I am behind schedule with my work. I attribute a good bit of this to
my vices as a developer, and just as much of the problem to my good
attributes. I place an equal portion of the blame on SOAP.

Striving for the goal of Beautiful Code, we can find ourselves lost on
the way to actually writing something that gets the job done. Throwing
away perfectly working code, because an alternative way to achieve the
same results is more elegant isn't something that we might see as a bad
idea. If the code is more l33t now, it will give us less trouble
tomorrow when we need to port it to my toaster. We'll use anything to
justify the overworking for code beauty.

.. figure:: /images/a_journey.jpg
    :alt: A fork in the road
    :align: right

Is it always worth it? How beautiful is enough and when are
we just wasting our time (and money)?

There are terms thrown around like "elegant" and "pythonic" to measure
the quality of code with no attention to the code actually reaching the
goal it sets out to perform. The code may work, but that doesn't make
the code good code. Without a sense of time, scale, and the big picture,
the search for good code can overshadow any good developer's work
towards working code.

However, as any issue as a flip side, those developers getting lost
are doing so in the name of a good fight: the first against bad code. We
might get lost and never complete our code, or complete it late, but we
do so with the complete belief that it was worth it. The code took
several weeks longer to develop, but just look at how beautiful it is.
Without the struggle for good code, our working, bad code would
eventually overshadow us just as much and consume our time with
maintenance, refactoring, and the mother of all frustrations in coding:
trying to read your own work.

I am wrapping up some SOAP-heavy work and the path to completing it
has been a testimony to the struggle of balance in code. Recent
refactorings of the actual SOAP response processing ended with a good
chunk of bad code. I don't like the way I'm doing lots of things, or the
fact that it doesn't parse corner cases the service I'm using doesn't
even use. The code is not the beautiful code I would like to call my
own, but the code is working code and does everything it needs to do. I
had to bite my own hand to keep the refactoring to a minimal and focus
solely on the aspects of functional goals, ignoring aesthetics.

Be careful on the road to good code. Somewhere along the way, you can
easily get lost and never reach the point of having actual, working
product. Sure, the code will be incomplete, but it will be a fragment of
beauty. Learn the value of a completed mediocre code set over the
eternal development of more beautiful code, which does exactly the same
thing.
