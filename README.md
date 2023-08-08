# Middleware in Django

## Table Of Content

- [What Is Middleware](#what-is-middleware).
- [Usage Of Middleware](#usage-of-middleware).
- [How To Write a Middleware in Django](#how-to-write-a-middleware-in-django).
- [Queries/Params in Django URI]().
- [Useful Things In Python]().

---

## What Is Middleware

>It’s a light, low-level “plugin” system for globally altering Django’s input or output. [Official Docs](https://docs.djangoproject.com/en/4.2/topics/http/middleware/).

- Middle Process between `Request` and `Response`.
- It can Kill the process between receiving Request and sending response, according to some conditions.
- The order in `MIDDLEWARE` array in `settings.py` is very **IMPORTANT**.
- Each middleware component is responsible for doing some specific function.

---

## Usage Of Middleware

During the request phase, before calling the view, Django applies middleware in the order it’s defined in MIDDLEWARE, top-down.

You can think of it like an onion: each middleware class is a “layer” that wraps the view, which is in the core of the onion. If the request passes through all the layers of the onion (each one calls get_response to pass the request in to the next layer), all the way to the view at the core, the response will then pass through every layer (in reverse order) on the way back out.

If one of the layers decides to short-circuit and return a response without ever calling its get_response, none of the layers of the onion inside that layer (including the view) will see the request or the response. The response will only return through the same layers that the request passed in through.

---

## How To Write a Middleware in Django

1. Create a folder in Application name it `middlewares`.
2. Create a file in that folder, name it `middleware.py`.
3. In this file, write the middleware, function or class:

```python
def simple_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware
```

4. Register this middleware in `settings.py`:

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    ...
    ...
    ...
    'My_MIDDLEWARE_MIDDLEWARE_FUNCTION',
]
```