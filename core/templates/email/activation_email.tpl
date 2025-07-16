{% extends "mail_templated/base.tpl" %}

{% block subject %}
Account activation
{% endblock %}

{% block body %}
Click the link below to activate your account:
http://127.0.0.1:8000/accounts/api/v1/activation/confirm/{{ token }}
{% endblock %}

{% block html %}
<p>Click the link below to activate your account:</p>
<p><a href="http://127.0.0.1:8000/accounts/api/v1/activation/confirm/{{ token }}">
Activate Account</a></p>
{% endblock %}
