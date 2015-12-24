Asyncronous Database Records
############################
:date: 2006-11-14 07:31
:author: Calvin Spealman (noreply@blogger.com)
:tags: database, axiom
:slug: asyncronous-database-records

Through persistence systems, notably Divmod's Axiom project, i have
been experimenting with the idea of asynchronous request of items which
may or may not exist for some time. The idea is an abstraction of a
terrible first idea for "persistent deferreds," which my very suggestion
of lead to horrible responses over in #twisted, but well deserved, I now
believe.

The concept is similar but perhaps simplified for the limitations and
complications involved. Operations may return an "asyncronous item,"
which in my implementation is done by an Item implementing the
IAsyncronousOperation ("operation" may be replaced with "Item")
interface. This is akin to returning a deferred. The item allows the
caller to control the response to the availability of the item, but in a
way that can survive server crashes and reboots, and is otherwise a
persistent record, and not an emphemeral object.

Borrowing additionally from Twisted, the asynchronous results can
support both positive and negative handlers, set for managing the result
as success or error. The creation of these handlers constitutes an
additional asynchronous result, which can be used to chain handlers, akin
to the callback chains of Twisted. In the event that the requested item
is ready, which is either immediately or in the future, the appropriate
handler is called and the asynchronous result handlers are cleaned up.

I will release the code soon, when the rest of the unittests are
complete and an example use-case can demonstrate the usefulness. I have
gotten some negative reaction from this one, and I really hope it can be
attributed to misconceptions of my intent and failure to consider the
right use-cases. Hopefully I can remedy this.
