Dead To Me! DomNomNom
#####################
:date: 2014-11-07 05:28
:author: Calvin Spealman (noreply@blogger.com)
:tags: web development, programming, software, dead to me
:slug: dead-to-me-domnomnom
:category: technology
:status: published

DomNomNom was a toy templating tool for front-end web applications I
built during a long ride in the passenger seat. The idea was to build a
templating system that required minimal, and in many cases, no template
at all. I wanted to see if it was possible to map data directly into
markup structures based purely on semantics.

For example, instead of some mark up that rendered a title into the page
like ``{{ title }}`` we might just map the ``<h1>`` tag to the title in the data
binding.

.. code-block:: javascript

   $(“body”).domnomnom({
      “h1”: “This is the title”,
   });

And it was really easy to get this basic setup in place quickly. I began
to take it further. I allowed mapping lists of data, which would clone
an element instead of simply inserting the text contents into it.
Suddenly I could render tables and lists with ease.

.. code-block:: javascript

   “ul”: {
      “li”: [“one”, “two”, “three”],
   }

And the markup’s original ``<li>`` would function as a template to clone for
this content. It was very clean to write templates for, because they
were just mark-up with dummy data and content in them. This meant a
designer could build the templates with whatever tools they wanted and
the data could just get pumped into it.

DomNomNom in its final state supports mapping syntax that can handle
attributes and properties, so you can map into form fields and the like.
There are also controls capable of changing the order cloned elements
are inserted and allowing the clone templates to be controlled better.
If I removed the empty lines for formatting, the whole thing would come
in under 100 lines of Javascript.

I built this on jQuery, but if I re-did this based on modern browsers
with querySelector it probably wouldn’t grow by more than a dozen lines,
and would be a lot faster.

`Check it out, if just to see. <https://github.com/ironfroggy/domnomnom>`__
