# -*- coding: utf-8 -*-
"""
    spacepaste.urls
    ~~~~~~~~~~~~~~~

    The URL mapping.

    :copyright: 2007-2008 by Armin Ronacher.
    :license: BSD
"""
from werkzeug.routing import Map, Rule

urlmap = Map([
    # paste interface
    Rule('/', endpoint='pastes/new_paste', methods=['GET', 'POST', 'PUT']),
    Rule('/+<language>', endpoint='pastes/new_paste', methods=['GET', 'POST', 'PUT']),
    Rule('/show/<identifier>/', endpoint='pastes/show_paste'),
    Rule('/raw/<identifier>/', endpoint='pastes/raw_paste'),
    Rule('/compare/', endpoint='pastes/compare_paste'),
    Rule('/compare/<new_id>/<old_id>/', endpoint='pastes/compare_paste'),
    Rule('/unidiff/<new_id>/<old_id>/', endpoint='pastes/unidiff_paste'),
    Rule('/tree/<identifier>/', endpoint='pastes/show_tree'),

    # captcha for new paste
    Rule('/_captcha.png', endpoint='pastes/show_captcha'),

    # xmlrpc and json
    Rule('/xmlrpc/', endpoint='xmlrpc/handle_request'),
    Rule('/json/', endpoint='json/handle_request'),

    # static pages
    Rule('/removal/', endpoint='static/removal'),

    # colorscheme
    Rule('/colorscheme/', endpoint='pastes/set_colorscheme'),
])
