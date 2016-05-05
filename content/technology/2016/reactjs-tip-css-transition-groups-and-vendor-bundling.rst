ReactJS Tip: CSS Transition Groups and Vendor Bundling
######################################################
:status: published
:date: 2016-05-04 22:39
:category: technology
:tags: reactjs,tip,javascript,es6,programming,web development
:slug: reactjs-tip-css-transition-groups-and-vendor-bundling
:title: ReactJS Tip: CSS Transition Groups and Vendor Bundling

Every developer finding their way around ReactJS is going to come across CSS Transition Groups
sooner or later. These helpful components built by the ReactJS team but distributed separately
help to manage animations related to adding or removing elements from a list. This is important
in ReactJS, because the virtual DOM reuses nodes as much as it can, meaning what seems like a
new element but really be reusing nodes underneath.

You can read all about the `ReactCSSTransitionGroup <https://facebook.github.io/react/docs/animation.html>`_ at the React documentation, but I want
to note about one way you might trip integrating it with your project: **building vendor bundles
for your dependencies.**

If you use `Browserify <http://browserify.org/>`_ to bundle your own code and its dependencies
for distribution, you may be using the vendor bundle pattern. This is the practice of separating
your distribution into two bundles: one containing your dependencies, including ReactJS itself,
and one with your own project code. This is a good pattern because you can rebuild just your
project bundle during development, allowing you to iterate much faster without rebuilding a large
number of non-changing dependencies.

This tip is about what happens when you move to add ``ReactCSSTransitionGroup`` to your project
by first installing the package.

.. sourcecode:: bash

    npm install --save-dev react-addons-css-transition-group

and import this in the packages where you need to use it.

.. sourcecode:: javascript

    import ReactCSSTransitionGroup from 'react-addons-css-transition-group';

And now you have fundamentally broken your project. Why? Because the ``react-addons-css-transition-group`` module itself depends on ``react`` creating a second copy
of ReactJS in your application bundle, in addition to the copy already in your vendor bundle.
Operations through the CSS Transition Group will fail in strange ways, as happens when you have
multiple copies of ReactJS in a single page.

The solution is simply to add this new module to your vendor bundle.

.. sourcecode:: javascript

    var vendor = browserify({
        debug: false,
        require: ['react', 'react-dom', 'react-addons-css-transition-group'],
    });
