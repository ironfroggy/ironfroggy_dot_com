Five Web Technologies I Need To Learn More About
################################################
:status: published
:date: 2016-05-08 13:00
:category: technology
:tags: programming,web development,javascript
:slug: web-technologies-i-need-to-learn-more-about
:title: Web Technologies I Need To Learn More About

I like to think I'm a good web developer. Getting here was the result of experience,
practice, and constant curiousity. Lately, I've wondered if the passive nature of that
curiousity has run its course. The pace and breadth of changing technologies as a web
developer can be both breathtaking and overwhelming at times. What do I need to know
about WebAssembly, WebGL 2.0, or the differences between Browserify and Webpack?

Do I need to know about any of them at all? How do I learn enough about each just to
understand if its something I need to understand even more deeply?

Beginning an effort to make that ever driving curiousity more directed, here's a list of
things I don't know enough about, but would like to study better.

Webpack
=======

**I know** that Webpack can replace Browserify and recently have understood it may replace
some (or all?) the ways I use Gulp today.

**I don't know** if the change would impact more projects beyond the build scripts or how
much time or effort would be involved with the change.

**I want to know** what solid advantages Webpack would bring other than just being "new and shiny".
I'm specifically interested in how Webpack can handle non-Javascript assets, and how this
might make it easier to isolate collections of componenets that pull in both behavior and styling
together.

Redux
=====

**I know** redux is a novel tool for managing all the data in a React application in a single
store, focused on immutable operations that enforce consistent operations on your data to make
testing and working with your componenets supposedly much easier.

**I don't know** some details about how to use Redux, like how to combine multiple components
from different sources if they have to share a single giant store.

**I want to know** if I can introduce Redux into projects without creating a huge learning curve
for teammates that may have less interest in the whole ecosystem than I.

Material UI
===========

**I know** that Material looks clean (at the very least I know it doesn't just look like
Bootstrap) and that Material-UI provides an implementation via React and could give me a big
boost getting started on building larger applications.

**I don't know** if Material-UI's reliance on Sass would impose a requirement on me, which might
be a problem because we've been a Less shop for years.

**I want to know** how easily we could use Material-UI as a basis to build collections of styled
components for each project, especially how much we can customize Material widgets, build more
complex widgets out of them, and style them without mucking with the original Sass.

Web Workers and Service Workers
===============================

**I know** that Web Workers and Service Workers bestow amazing new abilities to web applications
and I know a little about the lifecycle of a worker and its communication with the host page.

**I don't know** anything about Service Workers, other than their building on the foundation the
Web Workers laid out.

**I want to know** more about using Service Workers to control offline support, caching, and
optimizing page load times. I'm especially interested in using them to get a handle on long load
times on mobile and for larger, complicated Single Page Applications.

Sass and Stylus compared to Less
================================

**I know** that Less has served me well and been my preferred CSS precompiler for a long time,
but that decision and the environment it was made in was a half a decade past. For the same
reasons I needed to evaluate and focus on one options then, I need to do the same thing now that
the landscape has changed.

**I don't know** if the comparisons I made between Less and Sass five years ago are still valid
today. I don't know how Stylus, the new kid on the block, measures up between them. I don't know
if my preference for Less is holding me back because, despite what I'd prefer, its definitely the
least popular and the move of Bootstrap from Less to Sass might be a nail in the coffin.

**I want to know** what might have changed about Sass and how it compares to the evolution of Less
over the last few years. More so, I want to learn about Stylus. In the end, I want to figure out
if either Sass or Stylus are improvements enough to be worth the effort and pain of jumping ship.
