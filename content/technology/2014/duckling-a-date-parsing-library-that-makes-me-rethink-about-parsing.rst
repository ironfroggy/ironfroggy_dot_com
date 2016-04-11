Duckling, A Date-Parsing Library That Makes Me Rethink About Parsing
####################################################################
:date: 2014-10-06 01:02
:author: Calvin Spealman (noreply@blogger.com)
:tags: software development, programming, opinion
:slug: duckling-a-date-parsing-library-that-makes-me-rethink-about-parsing
:status: published
:category: technology


Earlier this week I ran across a really fascinating project called
`Duckling <http://duckling-lib.org/>`__. This isn't the
`Duckling <http://duckling.us/>`__ project that *I* work on, but the
coincidental name sameness probably caught my attention! Duckling is a
date parsing library for Clojure, but it handles date parsing in a
fairly unique fashion.

From the Duckling website:

| Duckling is “almost” a \ `Probabilistic Context Free Grammar <http://en.wikipedia.org/wiki/Stochastic_context-free_grammar>`__\ .

Although I am no NLP expert (it is on my long and growing list of
things to study *one of these days)*, I was able to get the just from
the explanation and the examples combined. Just look at some of the
strings Duckling is able to successfully parse:

| “the 1st of march”
| “last week”
| “a quarter to noon”
| “thirty two celsius”
| “2 inches”
| “the day before labor day 2020”

These don't even have to be dates. Duckling's approach is generalized
in a way that the library itself doesn't require special handling of
dates, only that it's training set includes sufficient samplings of date
(and other) text.

What stands out to me is that libraries like this are not just solving a
problem, but are actually **solving the problem of solving the
problem**. Programmers shouldn't spend their time parsing a million
different ways language can describe the same or very similar things,
because software can do it for us. And, as programmers, we need to be
more aware about what the computers we work with every day are really
capable of. When the compiler was invented, programmers were worried
they're jobs would become obsolete, but look at us: we still have barely
progressed, and some times I worry that is on purpose.

These little problems don't have to be hard, but by insisting that we
keep re-solving them in the most difficult and manual ways, we're
severely limiting the upward potentials of our craft.

Along similar thoughts I recently came across `Fix My
JS <http://goatslacker.github.io/fixmyjs.com/>`__, which automatically
lints and *actually fixes errors in* your Javascript.  More of this
please! Programming tools can be so much more advanced than they are
today, but instead of seeing any real progress, we just see new text
editors copying a new combination of feature sets of older text editors.

|image0|

We can do so much better. Let's see more of this!

|image1|

.. |image0| image:: /images/scott-pilgrim-bored.gif

.. |image1| image:: /images/jack-thumbs-up.gif
