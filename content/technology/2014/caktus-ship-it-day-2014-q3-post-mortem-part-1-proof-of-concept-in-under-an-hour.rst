Caktus Ship It! Day 2014 Q3 Post-Mortem - Part 1: Proof of Concept in Under an Hour
###################################################################################
:date: 2014-10-13 22:29
:author: Calvin Spealman (noreply@blogger.com)
:tags:  html5, caktus group, WebRTC, sharptune, ship it day
:slug: caktus-ship-it-day-2014-q3-post-mortem-part-1-proof-of-concept-in-under-an-hour
:status: published
:category: technology


Today was one of our very fun `Ship It!
Day <http://www.caktusgroup.com/blog/2012/10/01/planning-our-first-shipit-day-caktus/>`__ events
at Caktus Group and the first in our new office. It snuck up on a lot of
us, what with the busy move we're still settling down from, but it also
is a great chance to unwind and to really enjoy our new shared
workspace.


I'm going to start ending these events with a personal post-mortem on
what I worked on. I decided to learn about WebRTC by building a tool I'd
love to have with friends: a shared music player. The problem is simple:
some of us think the room is to quiet and some of us like quiet. What we
need is a way to play music together with headphones.

The goal was a simple app that can play MP3s. Everyone with the app
open should be able to play songs and everyone connected would listen at
the same time. We all hear the same thing. If someone leaves, they'll
take their music with them.

So, I set about this yesterday afternoon (when our Ship It festivities
officially begin) and I had a vague idea where I wanted to start. I had
seen an interesting proof-of-concept called instant.io which provided
file sharing in the browser. What made it novel from other demos was its
use of BitTorrent as the sharing mechanism, so it could be used to
effectively distribute a large file to a large number of recipients
efficiently!

My starting theory was "BitTorrent combined with Winamp, in your Browser"

So I set on this task by cloning the
`instant.io <http://instant.io/>`__ repository and running it locally,
which was a little more trouble than I expected. The actual setup of the
project was pretty odd, and depended on things specific to the owners
machine. What I did learn from instant.io was to find my way to the
WebTorrent project, on top of which instant.io was built.

I cleaned up the repository I had cloned to run a bit easier on my
machine and started pulling examples from the WebTorrent website. I
quickly got the file sharing working locally, dropping files onto one
browser and seeing download links appear in the second.

So far, so good!

The next step was rudimentary music playing. I dropped a simple HTML5
audio tag into the page

.. code-block:: html

    <audio controls />

And took a look at where the instant.io code was rendering its
download links after completing the transfer of a file from one peer to
the next. It was easy enough to find where it looped through the files
of a completed torrent and wrote the links into the page.

.. code-block:: javascript

    torrent.files.forEach(function (file) {
        file.createReadStream().pipe(concat(function (buf) {
            var a = document.createElement('a')
            a.download = file.name
            a.href = URL.createObjectURL(new Blob([ buf ]))
            a.textContent = 'download ' + file.name
            log.innerHTML += a.outerHTML
        }))
    })

A torrent can contain multiple files, and that was a fact that I had
neglected, but for the current testing I just assumed that I'm only
dropping one file at a time and I just take the first file in the
torrent. It was very easy to assign the Data URI being generated here to
the audio tag and trigger playback.

.. code-block:: javascript

    var file = torrent.files[0]
    file.createReadStream().pipe(concat(function (buf) {
        var a = document.querySelector('audio')
        a.src = URL.createObjectURL(new Blob([ buf ]))
        a.play()
    }))



Success! I had, in less than an hour, built a simple tool that lets a
bunch of people drop any MP3 into their browser window and all be
listening to the same song in just a few seconds. It worked great, but I
had a lot of work ahead of me.

- **Part 1: Proof of Concept in Under an Hour**
- Part 2: `Playlists and Reseeding Songs <./caktus-ship-it-day-2014-q3-post-mortem-part-2-playlists-and-peers.html>`__
- Part 3: Two Steps Back and Three Steps Forward

.. raw:: html

   </p>
