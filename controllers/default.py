# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# -------------------------------------------------------------------------
# This is a sample controller
# - index is the default action of any application
# - user is required for authentication and authorization
# - download is for downloading files uploaded in the db (does streaming)
# -------------------------------------------------------------------------
import soundcloud

def signin():
# create client object with app credentials
    client = soundcloud.Client(client_id='M0gen3egUbJm4q7oXlWr8Dxt2Mr2ufCW',
                          client_secret='qolACQko5MrQzXDF2aZCDXkbh4awdMfq',
                         redirect_uri='https://ec2-54-213-123-55.us-west-2.compute.amazonaws.com:8000/mixin/default/index/login')
# redirect user to authorize URL
    redirect(client.authorize_url())
    #return dict()
    
def play():
    import soundcloud

   # import soundcloud

# create a client object with your app credentials
    client = soundcloud.Client(client_id='M0gen3egUbJm4q7oXlWr8Dxt2Mr2ufCW')

# fetch track to stream
    track = client.get('/tracks/293')

# get the tracks streaming URL
    stream_url = client.get(track.stream_url, allow_redirects=False)

# print the tracks stream URL
    print stream_url.location
    
# create a client object with your app credentials
    #client = soundcloud.Client(client_id='M0gen3egUbJm4q7oXlWr8Dxt2Mr2ufCW')

# get a tracks oembed data
    #track_url = 'http://soundcloud.com/forss/flickermood'
    #embed_info = client.get('/oembed', url=track_url)

# print the html for the player widget
    #print embed_info['html']

def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
#  client = soundcloud.Client(client_id='M0gen3egUbJm4q7oXlWr8Dxt2Mr2ufCW',
   #                       client_secret='qolACQko5MrQzXDF2aZCDXkbh4awdMfq',
    #                     redirect_uri='https://ec2-54-213-123-55.us-west-2.compute.amazonaws.com:8000/mixin/default/index/login')
# redirect user to authorize URL
    #redirect(client.authorize_url())
    play()

    if (auth.is_logged_in()):
        redirect(URL('home'))
    form = auth()
    if response.title:
        welcomemessage = "Welcome to %s" % response.title
    else:
        welcomemessage = "Welcome"
    #if form.process().accepted:
    #    redirect(URL('home'))
    return dict(message=T(welcomemessage), form=form)


def user():
    # Chapter 09 Authorization
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())

@auth.requires_login()
def home():
    return dict(message=T('Hello %(first_name)s' % auth.user))
    #return dict(message=T("Hello %s", % auth.user))
    #return dict(message=('Hello'))

@auth.requires_login()
def musicroom():
    return dict(message=T('This is the music room'), message2=T('Thanks for coming to %(first_name)s\'s music room' % auth.user))

@auth.requires_login()
def about():
    return dict()

@auth.requires_login()
def contact():
    return dict()

@auth.requires_login()
def mbrain():
    return dict()

@auth.requires_login()
def sdinay():
    return dict()

@auth.requires_login()
def ryanho():
    return dict()

@auth.requires_login()
def jli306():
    return dict()

@auth.requires_login()
def katakeda():
    return dict()

@auth.requires_login()
def cdwheele():
    return dict()

@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()
