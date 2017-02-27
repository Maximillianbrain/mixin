# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# ----------------------------------------------------------------------------------------------------------------------
# Customize your APP title, subtitle and menus here
# ----------------------------------------------------------------------------------------------------------------------

response.logo = A(IMG(_src="/mixin/static/images/logo.png", _width="65"),
                  _class="navbar-brand", _id="mi-navbar-logo", _href="http://www.mixin.com/")
response.title = request.application.replace('_', ' ').title()
response.subtitle = ''

# ----------------------------------------------------------------------------------------------------------------------
# read more at http://dev.w3.org/html5/markup/meta.name.html
# ----------------------------------------------------------------------------------------------------------------------
response.meta.author = myconf.get('app.author')
response.meta.description = myconf.get('app.description')
response.meta.keywords = myconf.get('app.keywords')
response.meta.generator = myconf.get('app.generator')

# ----------------------------------------------------------------------------------------------------------------------
# your http://google.com/analytics id
# ----------------------------------------------------------------------------------------------------------------------
response.google_analytics_id = None

# ----------------------------------------------------------------------------------------------------------------------
# this is the main application menu add/remove items as required
# ----------------------------------------------------------------------------------------------------------------------

response.menu = [
    (T('Home'), False, URL('default', 'home'), [])
]

DEVELOPMENT_MENU = True


# ----------------------------------------------------------------------------------------------------------------------
# provide shortcuts for development. remove in production
# ----------------------------------------------------------------------------------------------------------------------

def _():
    # ------------------------------------------------------------------------------------------------------------------
    # shortcuts
    # ------------------------------------------------------------------------------------------------------------------
    app = request.application
    ctr = request.controller
    # ------------------------------------------------------------------------------------------------------------------
    # useful links to internal and external resources
    # ------------------------------------------------------------------------------------------------------------------
    response.menu += [
        (T('About'), False, URL(app, 'default', 'about')),
        (T('Contact'), False, URL(app, 'default', 'contact')),
        (T('Team Members'), False, '#', [
            (T('Maximillian Brain'), False, URL(app, 'default', 'mbrain')),
            LI(_class="divider"),
            (T('Shanee Dinay'), False, URL(app, 'default', 'sdinay')),
            LI(_class="divider"),
            (T('Ryan Ho'), False, URL(app, 'default', 'ryanho')),
            LI(_class="divider"),
            (T('Jinlin Li'), False, URL(app, 'default', 'jli306')),
            LI(_class="divider"),
            (T('Kaitaku Takeda'), False, URL(app, 'default', 'katakeda')),
            LI(_class="divider"),
            (T('Cameron Wheeler'), False, URL(app, 'default', 'cdwheele')),
        ]),
    ]


if DEVELOPMENT_MENU:
    _()

if "auth" in locals():
    auth.wikimenu()
