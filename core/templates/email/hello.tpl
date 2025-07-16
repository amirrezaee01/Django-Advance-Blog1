{% extends "mail_templated/base.tpl" %}

{% block subject %}
Hello {{ user.name }}
{% endblock %}

{% block body %}
account activation
{% endblock %}

{% block html %}
{{token}}
{% endblock %}
