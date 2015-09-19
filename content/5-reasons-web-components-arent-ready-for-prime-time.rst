5 Reasons Web Components Aren't Ready for Prime Time
####################################################
:date: 2013-11-10 14:22
:author: Calvin Spealman (noreply@blogger.com)
:category: technology
:tags: web development, html5, javascript, x-tags, community, polymer, web components
:slug: 5-reasons-web-components-arent-ready-for-prime-time

Wow! Web Components are amazing! Honestly, despite the negative title
of this post I'm absolutely floored with excitement for this new set of
technologies.
This post is my exercise in grounding my excitement a bit with some
reality discovered in actually using them in a serious project, and the
issues we've run against and had to deal with.
Web Components are an important part of the future of web development,
and libraries like Polymer and X-Tags mean we can use much of their
power today, without waiting browser support (which is already under
way!) Like so many new technologies, this is also incomplete.
It may be fair, it would be more accurate to say **the ecosystem
around Web Components is not mature**, than to blame Web Components
directly. Ecosystems are extremely important. Therefore, the items
listed here are the parts of an ecosystem that I believe we need built
around this new set of technologies.

Missing Item 1: Routing
-----------------------

Now this one took me by surprise because, at the surface, routing
seems to have little to do with defining custom elements and behavior.
So how does this work its way into missing bits of the Web Component
ecosystem? The lack of routing crept into our project from two facets:
**the frameworks you might otherwise use happen to include routing** and
**routes feel like they could naturally map into custom elements**.
At first the lack of a routing tool seemed simply to be that I wasn't
using a framework that already provided one, like AngularJS. That didn't
seem like anything to do with the choice of Web Components, it was just
an indirect effect of not having gone with a library that included one
in its utility belt.
I brought in a library of my own making, which I've re-used in various
projects for years, called Hashtrack.js and I'm pretty happy with it.
Pretty quickly it dawned on me that the natural thing for a route to
map to? A custom element encapsulating a page within your app. Does that
mean a collection of elements and displaying one mapped to by a route or
instantiating a given element, perhaps from a template, in response to
routing? We've taken the former option at the moment, but I'm thinking
the later would be preferable. **This makes me wonder if routing should
be an intrinsic aspect of custom elements**.

Missing Item 2: Outward Data Binding
------------------------------------

What do I mean by *Outward Data Binding?*

The popular model emerging in the use of custom elements is to
utilize attributes as the primary input, and this is great. Attributes
already serve this purpose for existing elements, defining behavior
characteristics and other factors in how a given element is to behave.
It makes perfect sense to use attributes as the primary avenue getting
data into our components.
But... *how do we get changes to that data back out?*

The canonical example is probably trying to reproduce the popular and
most basic example from AngularJS: Given a text input and a span tag,
how do we get changes in the input reflected in the span's text?

..

    <message-form name="Frank">
      <template>
        <label>Name: <input value="{{ name }}"></label>
        <div>
          Hello, {{ name }}! It is nice to meet you.
        </div>
      </template>
    </message-form>

This is something Polymer is already trying to solve, via their Template
Binding facilities. These work great! I tend to think they're on to
something good. Unfortunately, this is one part of Polymer that is not
yet backed by any kind of standards negotiation, not even in an early
draft. I don't have great hopes that something quite so opinionated will
end up with W3C support, but maybe I'll be surprised.

Or, **maybe template binding doesn't need to be standard to be
valuable**. Maybe this is a great example of the ecosystem to be built
around Web Components. My final issue with Polymer template binding is
I'm not sure how it, and the mutation observers it relies on, work on a
wider set of browsers actually in use today.

Supporting older Android devices that Polymer ignores, we don't have
template binding available (dang!) but I've replicated part of the
spirit of it. Element templates are extracted and rendered into new
instances, and re-rendered when any of the attributes found. This has
proven (I think, admittedly with bias) to be a simple solution to
getting data *inward* but has fallen utterly flat when trying to get it
back out in as simple a way.
Maybe this is why the Template Binding library from Polymer project is
so very *not* simple!

Missing Item 3: Templates are Complicated by Custom Elements
------------------------------------------------------------

*Speaking of templates... oh boy do Custom Elements confuse them!*
*
*\ The upgrade process involved in locating and initializing the
elements you've registered can wreck havoc on our established template
libraries. The problems are numerous.
Template rendering on input changes means re-drawing your elements
into the DOM, and *all* of the other custom elements they might contain.
Every time you do this, your elements are going to be re-initialized.
**Dealing with the complexities involved with all of this logic running
repeatedly, without unwanted side effects being invoked more often than
intended, is a huge hassle.**
Our familiar model of rendering from a plain text template outputting
DOM to insert into the page doesn't sit well with our lively new Web
Components. This is why, if I understand correctly, the approach of
Template Binding acting upon live DOM nodes, rather than textual
templates, works better. We need to replace our rendering with binding.
For now, I'm using Mustache templates, but being careful to give my
elements side-effect free initializes.

Missing Item 4: Decent Browser Support
--------------------------------------

The elephant in the room. Polymer explicitly decides to support only
the most modern browsers, and while some of their polyfills do work on a
wider range of clients, important bits like ShadowDOM absolutely do not.
X-Tags provides a broader support of browsers, but covers a smaller set
of features and provides us with a lot less suggested convention to jump
start the architecture of a project using something so new.
Polymer is essentially assuming whatever the new hotness on the block
is that week. IE 10/11 only, newest Firefox and Chrome and Opera. This
is a part of the idea that Polymer is a plan for the future, even though
so much of it is useful today.
X-Tags, on the other hand, claims to support a much better range.

-  Firefox 5+
-  Chrome 4+
-  Android 2.1+
-  Safari 4+
-  IE 9+
-  Opera 11+

This isn't actually completely accurate! It is pretty close, but I've
found some issues where suggested features of x-tags don't work on many
browsers. One example is the <template> tag shown in the documentation,
but which many of these browsers don't support. Don't fear, it is `easy
to polyfill <http://jsfiddle.net/brianblakely/h3EmY/>`__! Still, this is
a bit disheartening.

*(hint: x-tags should really include this polyfill)*



Missing Item 5: A Community
---------------------------

And this, really, is the killer missing item.

You.

Web Components are a powerful idea, an inevitable advancement of our
browsers, and on the way today. They have their flaws, and there is a
lot of work to be done, but for the right projects in the right scope
with the right developer mindset, you can dip your toes in the warm
water.
Start building things. Blog about your successes. Blog about the
failures. Share the solutions and the things you find to fill the gaps.
Complain on the mailing lists when something is broken, but complain
with an idea how it could be fixed. Be a part of what is soon to be a
part of *all* our web development.
You can help fix this last missing item, and from this all the rest will
fall into place.
