# -*- coding: utf-8 -*-

#########################################################################
## This scaffolding model makes your app work on Google App Engine too
## File is released under public domain and you can use without limitations
#########################################################################

## if SSL/HTTPS is properly configured and you want all HTTP requests to
## be redirected to HTTPS, uncomment the line below:
# request.requires_https()

## app configuration made easy. Look inside private/appconfig.ini
from gluon.contrib.appconfig import AppConfig
## once in production, remove reload=True to gain full speed
myconf = AppConfig(reload=True)


if not request.env.web2py_runtime_gae:
    ## if NOT running on Google App Engine use SQLite or other DB
    db = DAL(myconf.take('db.uri'), pool_size=myconf.take('db.pool_size', cast=int), check_reserved=['all'])
else:
    ## connect to Google BigTable (optional 'google:datastore://namespace')
    db = DAL('google:datastore+ndb')
    ## store sessions and tickets there
    session.connect(request, response, db=db)
    ## or store session in Memcache, Redis, etc.
    ## from gluon.contrib.memdb import MEMDB
    ## from google.appengine.api.memcache import Client
    ## session.connect(request, response, db = MEMDB(Client()))

## by default give a view/generic.extension to all actions from localhost
## none otherwise. a pattern can be 'controller/function.extension'
response.generic_patterns = ['*'] if request.is_local else []
## choose a style for forms
response.formstyle = myconf.take('forms.formstyle')  # or 'bootstrap3_stacked' or 'bootstrap2' or other
response.form_label_separator = myconf.take('forms.separator')


## (optional) optimize handling of static files
# response.optimize_css = 'concat,minify,inline'
# response.optimize_js = 'concat,minify,inline'
## (optional) static assets folder versioning
# response.static_version = '0.0.0'
#########################################################################
## Here is sample code if you need for
## - email capabilities
## - authentication (registration, login, logout, ... )
## - authorization (role based authorization)
## - services (xml, csv, json, xmlrpc, jsonrpc, amf, rss)
## - old style crud actions
## (more options discussed in gluon/tools.py)
#########################################################################

from gluon.tools import Auth, Service, PluginManager

auth = Auth(db)
service = Service()
plugins = PluginManager()

## create all tables needed by auth if not custom tables
auth.define_tables(username=False, signature=False)

## configure email
mail = auth.settings.mailer
mail.settings.server = 'logging' if request.is_local else myconf.take('smtp.server')
mail.settings.sender = myconf.take('smtp.sender')
mail.settings.login = myconf.take('smtp.login')

## configure auth policy
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True

#########################################################################
## Define your tables below (or better in another model file) for example
##
## >>> db.define_table('mytable',Field('myfield','string'))
##
## Fields can be 'string','text','password','integer','double','boolean'
##       'date','time','datetime','blob','upload', 'reference TABLENAME'
## There is an implicit 'id integer autoincrement' field
## Consult manual for more options, validators, etc.
##
## More API examples for controllers:
##
## >>> db.mytable.insert(myfield='value')
## >>> rows=db(db.mytable.myfield=='value').select(db.mytable.ALL)
## >>> for row in rows: print row.id, row.myfield
#########################################################################

## after defining tables, uncomment below to enable auditing
# auth.enable_record_versioning(db)

mail.settings.server = settings.email_server
mail.settings.sender = settings.email_sender
mail.settings.login = settings.email_login

db.define_table('unidad_metrica',
   Field('nombre_unidadMetrica',unique='true'))

db.define_table('inventario',
   Field('material'),
   Field('cantidad','float'),
   Field('unidad_metrica',db.unidad_metrica))

db.define_table('edificio',
   Field('nombre'),
   Field('nomenclatura'))

db.define_table('lugar',
   Field('edificio',db.edificio),
   Field('espacio'),
   Field('referencia'),
   Field('extension_tlf', 'integer'))

db.define_table('area',
   Field('nombre'),
   Field('nomenclatura'))

db.define_table('supervisor',
   Field('area', db.area),
   Field('nombre'),
   Field('apellido'),
   Field('identificador'),
   primarykey=['identificador'])

db.define_table('empleado',
   Field('nombre'),
   Field('apellido'),
   Field('identificador'),
   Field('cargo'),
   Field('area', db.area),
   Field('tlf'),
   primarykey=['identificador'])

db.define_table('unidad',
   Field('nombre', unique='true'))

db.define_table('estatus_solicitud',
   Field('nombre_estatus',unique='true'))

db.define_table('prioridad',
   Field('nombre_prioridad',unique='true'))

db.define_table('espacio',
   Field('nombre_espacio',unique='true'))


db.supervisor.area.requires = IS_IN_DB(db, db.area.nombre)
db.empleado.area.requires = IS_IN_DB(db, db.area.nombre)
db.inventario.unidad_metrica.requires = IS_IN_DB(db, db.unidad_metrica.nombre_unidadMetrica)
db.lugar.edificio.requires = IS_IN_DB(db, db.edificio.nombre)
db.unidad_metrica.nombre_unidadMetrica.requires = IS_NOT_EMPTY()
db.espacio.nombre_espacio.requires = IS_NOT_EMPTY()
db.empleado.nombre.requires = IS_NOT_EMPTY()
db.empleado.apellido.requires = IS_NOT_EMPTY()
db.empleado.identificador.requires = IS_NOT_EMPTY()
db.inventario.material.requires = IS_NOT_EMPTY()
db.inventario.cantidad.requires = IS_NOT_EMPTY()
db.edificio.nombre.requires = IS_NOT_EMPTY()
db.edificio.nomenclatura.requires = IS_NOT_EMPTY()
db.area.nombre.requires = IS_NOT_EMPTY()
db.area.nomenclatura.requires = IS_NOT_EMPTY()
db.supervisor.nombre.requires = IS_NOT_EMPTY()
db.supervisor.apellido.requires = IS_NOT_EMPTY()
db.supervisor.identificador.requires = IS_NOT_EMPTY()
db.supervisor.area.requires = IS_NOT_EMPTY()
db.unidad.nombre.requires = IS_NOT_EMPTY()
db.prioridad.nombre_prioridad.requires = IS_NOT_EMPTY()
db.estatus_solicitud.nombre_estatus.requires = IS_NOT_EMPTY()
db.lugar.edificio.requires = IS_IN_DB(db, db.edificio.id, '%(nombre)s')
db.supervisor.area.requires = IS_IN_DB(db, db.area.id, '%(nombre)s')
db.empleado.area.requires = IS_IN_DB(db, db.area.id, '%(nombre)s')
db.inventario.unidad_metrica.requires = IS_IN_DB(db, db.unidad_metrica.id, '%(nombre_unidadMetrica)s')
db.area.nombre.requires = IS_NOT_IN_DB(db, db.area.nombre)
db.edificio.nombre.requires = IS_NOT_IN_DB(db, db.edificio.nombre)
db.unidad.nombre.requires = IS_NOT_IN_DB(db, db.unidad.nombre)
