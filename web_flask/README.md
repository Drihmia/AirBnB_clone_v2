# web_flask

# General

## What is a Web Framework
A web framework is a software framework designed to simplify the process of building web applications.

## How to build a web framework with Flask
Flask is a lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications.

## How to define routes in Flask
In Flask, routes are defined using the `@app.route()` decorator above a function, which becomes the view function for that route.

## What is a route
A route is a URL pattern that is used to load and display a certain page/view in a web application.

## How to handle variables in a route
Variables in a route are defined using angle brackets `<variable>` and can be accessed in the view function as arguments.

## What is a template
A template is a file that serves as a starting point for a new document. In the context of web development, it often refers to HTML files with placeholders for data that will be filled in when the page is rendered.

## How to create a HTML response in Flask by using a template
Flask uses the Jinja2 template engine. You can create a HTML response by defining a template in the templates folder and using the `render_template()` function in your view function.

## How to create a dynamic template (loops, conditions…)
Jinja2, the template engine used by Flask, supports control structures like loops and conditionals. You can use `{% for %}` for loops and `{% if %}` for conditionals.

## How to display in HTML data from a MySQL database
You can display data from a MySQL database in your HTML by first querying the database in your view function, passing the results to your template, and then using placeholders in your template to display the data.

