Publishing ES6 Modules to NPM
#############################
:status: published
:date: 2016-04-09 22:02
:category: technology
:tags: es6,javascript,web,web development,nodejs,programming
:slug: publishing-es6-modules-to-npm
:title: Publishing ES6 Modules to NPM

I had an adventure over the last couple days with ES6!

There was a pattern I'd already used in a few of my React projects to make ES6 classes a little
nicer. ES6 did a lot to make working with `this` mechanics nicer, but there was a still a gap that
bit me: the sugar provided by ES6 classes don't extend to keeping method bound to instances of the
class.

Maybe you, like me, would expect this to work:

.. code-block:: javascript

    class Counter {
        constructor() {
            this.count = 0
        }
        onClick() {
            this.count += 1
        }
    }
    counter = new Counter()
    document.querySelector('#add-button').onclick = counter.onClick

But, like non-class methods on any regular Javascript object, `onClick` will loose its binding to
the `Counter` instance. There are a few existing solutions to this, but I wanted one that didn't
change the syntax of defining a method on these classes.

Enter AutoBind, via my new NPM module `es6-class-auto-bind`:

.. code-block:: javascript

    import AutoBind from 'es6-class-auto-bind'

    class Counter extends AutoBind() {
        constructor() {
            this.count = 0
        }
        onClick() {
            this.count += 1
        }
    }
    counter = new Counter()
    document.querySelector('#add-button').onclick = counter.onClick

You can read all about the `AutoBind` class [at its NPM readme](https://www.npmjs.com/package/es6-class-auto-bind)
and you can read on to learn about what I learned to publish this ES6 module on NPM, consumable
by other ES6 (and even ES5) code.

The Problems of ES6 on NPM
==========================

For the moment, NPM is a tool for distributing and installing ES5 modules. While you can point
it at any types of files you want (some people have even used NPM to distribute C libraries!)
the mechanisms that install and then import those modules in NodeJS (or Browserify) are expecting
ES5 modules, so they won't do your users any good.

There are two problems we'll face shipping ES6 code directly.

First, most of the ES6 code we might ship would be completely useful for consumption by ES5 code.
My choice of ES6 shouldn't prohibit anyone from consuming my libraries. We want to publish something
that both new ES6 and legacy ES5 code can make use of without caring much about what's inside. And,
we want to do so without carrying build constraints on our users, like requiring they integrate
BabelJS into their pipeline when they haven't done so already.

Second, for those consumers of our module who already *are* using BabelJS or another transpiler to
ship their ES6 to ES5 runtimes, importing ES6 code installed by NPM is probably *not* going to work
out of the box! Browserify here is a big culprit, refusing to apply configured transform plugins to
packages installed from `node_modules/`, only to those from your own local project.

Now, I understand Webpack may be better about enabling this usecase, but I don't want to impose that
move to people still on Browserify (and I still want to support ES5 users), so I wanted a solution
that works for everyone.

How To Combine Packaging and Transformation
===========================================

The solution is to tranform our ES6 module to ES5 *before* publication, and idealy to automate this.
We want to transform it into an ES5 version of itself and tell NPM to publish *that* version of our
module, instead of the original ES6 version. Here's how we do it.

We'll put our two versions into a `src/index.js` and `build/index.js`. Transforming the first to
the second is straightforward with BabelJS, which we'll install first:

.. code-block:: bash

    npm install --save-dev babel-cli
    npm install --save-dev babel-preset-es2015
    npm install --save-dev babel-runtime
    node_modules/.bin/babel src/index.js > build/index.js

Now we have both versions, and we only need to tell NPM what we actually want a consumer to get when
they `require()` or `import` it.

.. code-block:: javascript

    "main": "./build/index.js",

Great! But we still need to make this happen automatically any time we issue an `npm publish`, never
allowing us to publish a version that isn't compiled from the most recent version of the ES6 source.

.. code-block:: javascript

    "scripts": {
        "compile": "node_modules/.bin/babel src/index.js > build/index.js",
        "prepublish": "npm run compile"
    }

We've defined two `npm run` scripts now: `compile` and `prepublish`. We can run `npm run compile` to
test our preparation any time, and NPM itself will invoke `prepublish` before any new version you
attempt to upload via `npm publish`. We've now configured our module to transform from ES6 to ES5
before publication to NPM, where it is consumable by any other project that needs it!

We're *almost* done at this point. There is a last step we can take to make the whole process more
consistent between ES5 and ES6 norms. The ES6 module syntax's `export` statement is largely
comparable to `exports.member = something` statements in NodeJS' ES5 modules, and BabelJS will
transform them appropriately. But `export` has a special form for exporting *one* member as a
default, to be handed to an importing module when it only asks for a single thing from the module.

.. code-block:: javascript

    import AutoBind from 'es6-class-auto-bind'

.. code-block:: javascript

    export default class AutoBind {

The problem is BabelJS transforms this by exporting these defaults with the obvious name
`"default"`, and accesses the `.default` member of a module when performing a default `import`. But,
this means ES5 code would need to access the `.default` member explicitly, with the unfortunate
`requires()` invoking as `require("es6-class-auto-bind").default`. We'd like to get rid of that
ugly `.default` at the end, obviously.

It turns out this is a behavior BabelJS *did* have but changed. It is also a behavior we can restore
through a plugin that re-implementes the deprecated behavior. I think allowing it to be optional
like this is just fine. We just need to install the plugin

.. code-block:: javascript

    npm install --save-dev babel-plugin-add-module-exports

And change our `compile` script to enable the plugin

.. code-block:: javascript

    "scripts": {
        "compile": "node_modules/.bin/babel src/index.js --plugin add-module-exports > build/index.js",
        "prepublish": "npm run compile"
    }

And, that's it. Everything works great now. This is how I was able to ship my ES6 `AutoBind` class
via NPM and install into other ES6 classes, seamlessly building my ES6 code across packages. Very
exciting!

Here's the whole portion of the `package.json` necessary to make this work.

.. code-block:: javascript

    "main": "./build/index.js",
    "scripts": {
        "compile": "node_modules/.bin/babel --plugins add-module-exports src/index.js > build/index.js",
        "prepublish": "npm run compile"
    },
    "devDependencies": {
        "babel-cli": "^6.7.5",
        "babel-plugin-add-module-exports": "^0.1.2",
        "babel-preset-es2015": "^6.6.0",
        "babel-runtime": "^6.6.1",

Stay subscribed for follow up posts on the subject, as I dig into how to expand this to:

* Ship a copy of the ES6 code in parallel and pull that into the project's own transform options
* Understand how to expand this approach to packages with more than one module
