# Django chunks documentation

## Preface

Think of it as flatpages for small bits of reusable content you might want to insert into your templates and manage from the admin interface.
This is really nothing more than a model and a template tag.

By adding `chunks` to your installed apps list in your Django project and performing a `./manage.py syncdb`, you'll be able to add as many "keyed" bits of content chunks to your site.

The idea here is that you can create a chunk of content, name it with a unique key (for example: `home_page_left_bottom`) and then you can call this content from a normal template.

### Why would anyone want this?

Well it essentially allows someone to define "chunks" (I had wanted to call it blocks, but that would be very confusing for obvious reasons) of content in your template that can be directly edited from the awesome Django admin interface.  Throwing a rich text editor control on top of it make it even easier.

## Installation and basic usage

1. Install package

    `` pip install git+git://github.com/shoker174/django-chunks.git``

2. Configure your settings file:

    ```
    INSTALLED_APPS += ['chunks']
    ```
3. Call chunks in the html template

    Usage example №1:
    ``` html
    {% load chunks_tags %}
    <html>
    	...
    	{% chunk "phone" %}
    	...
    </html>
	```
    Usage example №2:
    ``` html
    {% load chunks_tags %}
    <html>
    	...
    	{% get_chunk "phone" as phone %}
        {% if phone.content %}
        	<span>{{ phone.content }}</span>
        {% endif %}
    	...
    </html>
4. Apply migrations and run local server

    ```python
    python manage.py migrate chunks
    python manage.py runserver
    ```
5. Create chunks in admin interface

## Advansed usage
In many cases you may need in many chunks. Basic usage examples generate one request to database for each chunk -
this is a bad idea for large projects. For large progects your must use cached chunks.

1. Add context processor to settings.py

	```python
	TEMPLATES[0]['OPTIONS']['context_processors'] += ['chunks.context_processors.chunks_processor']
	```
2. Call chunks in the html template
	```html
    <html>
    	...
        {% if chunks.phone %}
        	<span>{{ chunks.phone.content }}</span>
        {% endif %}
    	...
    </html>
    ```
