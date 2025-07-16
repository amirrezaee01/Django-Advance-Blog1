{% extends "mail_templated/base.tpl" %}

{% block subject %}
Hello {{ user.name }}
{% endblock %}

{% block body %}
This is a plain text part.
{% endblock %}

{% block html %}
<p>This is an <strong>HTML</strong> part.</p>

{% endblock %}
