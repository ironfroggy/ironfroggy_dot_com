Design for Testing
##################
:date: 2006-11-08 07:31
:author: Calvin Spealman (noreply@blogger.com)
:tags: testing, programming, development
:slug: design-for-testing
:status: published
:category: technology

Good testing influences your design. Too many developers (and
managers) are stuck in the waterfall mentality of design, code, test,
and deploy. Forces across the industry are pushing to move the testing
phase to the beginning of this line, and many just don't understand how
that works. Testing should be the first consideration, and thus is
influential to all other aspects of the development process.

The problem with testing as a secondary consideration is the design
and architecture of the software never lends itself to proper testing
when you don't plan way ahead. The consideration of testing can drive
your design to be easier to test, but also can encourage generally good
programming practices and well-made designs in the architecture. We can
use a persisted class as a good example, because this is a use-case
where testing is very important, but we have to consider the burden of a
full database tied into the class we are testing.

When we develop our database item class before any testing is
considered, we create it fairly in a straight-forward manner. After
everything is coded, we decide to do some testing but we have a couple
problems to face. The first thing to concern us is that our class
inherits some ItemSchema super-class, and instances of it must exist in
context to some database, which creates a large dependency on the test
and thus leads to the test being unreliable. Secondly, we have many
functions not easily testable (perhaps they can only be confirmed by
locals within the function, which we can not access). We need to
redesign everything to solve these issues, but we could have avoided
this by using a more testable design in the first place.

To solve the first problem, we have to consider what we are actually
testing. We are not testing the persistence framework our application
utilizes, but just one ItemSchema sub-class we had to write. Obviously,
separation is key. We only care about the functionality we wrote into
the type, and we can extract all this into a mixin class, which our
original ItemSchema can inherit. However, in our tests, a special
TestItem class may also inherit it and perform the testing we need,
without bringing a database into the picture.

Tackling the second problem of individual functions, the solutions can
vary. If any internal data is important, perhaps it is too internal, and
the code generating it could be extracted into its own method, which we
can test independently. If our method does not return anything, perhaps
this is something it could return and thus we could test for it.

However, don't return things you do not need in production, as this
bloats the interface and inevitably some code will come to depend on
this contract that was only intended as a testing mechanism. It can even
be acceptable to wrap a returning method with a public API non-returning
version, simply to push a more stable API (it is easier to add returns
than remove them) to the consumers of the API.

We have to stop looking at the testing as a second, or third class
citizen in the steps we take in development. Our design, development
time-lines, and architecture should all be done with testing and quality
assurance first in mind. We must focus on how to ensure the stability
and accuracy of our code before we can ever trust it, and if we can not
trust it, all time developing it is a waste. It is this fact that
offsets all arguments by opponents of proper testing (yes, they exist)
who are afraid of the time wasted by testing. Wasted time is
illusionary, as we only see the time it takes but we don't see the time
it save us. However, isn't that the point?
