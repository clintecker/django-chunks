Think of it as flatpages for small bits of reusable content you might want to insert into your templates and manage from the admin interface.

This is really nothing more than a model and a template tag.

By adding `chunks` to your installed apps list in your Django project and performing a `./manage.py syncdb`, you'll be able to add as many "keyed" bits of content chunks to your site.

The idea here is that you can create a chunk of content, name it with a unique key (for example: `home_page_left_bottom`) and then you can call this content from a normal template.

===Why would anyone want this?===

Well it essentially allows someone to define "chunks" (I had wanted to call it blocks, but that would be very confusing for obvious reasons) of content in your template that can be directly edited from the awesome Django admin interface.  Throwing a rich text editor control on top of it make it even easier.

===Usage:===
{{{
{% load chunks %}
<html>
    <head>
        <title>Test</title>
    </head>
    <body>
        <h1> Blah blah blah</h1>
        <div id="sidebar">
            ...
        </div>
        <div id="left">
            {% chunk "home_page_left" %}
        </div>
        <div id="right">
            {% chunk "home_page_right" %}
        </div>
    </body>
</html>
}}}

This is really helpful in those cases where you want to use `django.contrib.flatpages` but you need multiple content areas.  I hope this is helpful to people and I'll be making minor edits as I see them necessary.
