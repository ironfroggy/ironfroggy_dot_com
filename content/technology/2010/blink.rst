Blink
#####
:date: 2010-07-19 18:51
:author: Calvin Spealman (noreply@blogger.com)
:tags: css, funny,  web
:slug: blink
:category: technology

.. raw:: html

   <style>
      @keyframes blinkit {
         from { opacity: 1.0; }
         50% { opacity: 0.0; }
         to { opacity: 1.0; }
      }
      blink {
         animation: blinkit 0.5s infinite;
      }
   </style>
   <blink>Blink!</blink>

**NOTE:** Please don't do this.

**UPDATE:** This original post has been updated to remove the old webkit only prefixes and to
work on all modern browsers.

The <blink> is back.

Thankfully, for you Firefox users, this won't work.

All of my webkit using readers see a blink tag, doing its blinking,
which webkit does not implement. This is all thanks to an evil snippet
of CSS:

.. code:: css

   @keyframes blinkit {
      from { opacity: 1.0; }
      50% { opacity: 0.0; }
      to { opacity: 1.0; }
   }
   blink {
      animation: blinkit 0.5s infinite;
   }

We can use our powers for good or for evil.

Sometimes, evil is just fun!

*EDIT: This might not work for everyone, even in webkit browsers. It
works less reliably when I actually post it, but it is still fun!*
