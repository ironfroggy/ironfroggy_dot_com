A short comment on the future of programming languages
######################################################
:date: 2006-03-05 18:23
:author: Calvin Spealman (noreply@blogger.com)
:category: technology
:tags: programming
:slug: a-short-comment-on-the-future-of-programming-languages

I've caught some recent articles and commentary asking a basic
question of "What's next for programming langauges?" and I though I'd
make a quick and short stab at a guess.

Considering a few elements to the soup that I think are key: the rise
of dynamic languages and rapid development, the prevelence of the
internet spreading word and use of multiple APIs and frameworks, and an
increasing need for portability over a range of targets. I think this
will lead to one inevitable move in software, but who makes it is
anyone's guess.

We're going to see first one, and then many, dynamic, binary-compiled
languages. We'll see things that allow two games to be written, one
using Direct3D and one using OpenGL, and to compile them for the same
target, using either. We'll see the ability for compilers to restructure
the original code in such a way that library APIs will be more than
calls to link to, but templates that will portray the intentions of the
programmers and be able to adapt them to the target in question.

I call this "Hard Linked Libraries", but I'm sure a dozen names will
surface. Python could make moves toward something like this, I'm sure.
But my guess is that eventually something will surface in .Net to do
things along these lines, probably using or extending generics.

I'll post more, and maybe some mockups. What do you think? Is this
likely or feasible or stupid?
