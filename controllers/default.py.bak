# -*- coding: utf-8 -*-
### required - do no delete
def user(): return dict(form=auth())
def download(): return response.download(request,db)
def call(): return service()
### end requires
def index():
    return dict()

@auth.requires_login()
def notifications():
    return dict()

@auth.requires_login()
def requests():
    return dict()

@auth.requires_login()
def catalogue():
    personal = db().select(db.empleado.ALL, orderby=db.empleado.nombre)
    edificio = db().select(db.edificio.ALL, orderby=db.edificio.nombre)
    inventario = db().select(db.inventario.ALL, orderby=db.inventario.material)
    area = db().select(db.area.ALL, orderby=db.area.nombre)
    supervisor = db().select(db.supervisor.ALL, orderby=db.supervisor.nombre)
    unidad = db().select(db.unidad.ALL, orderby=db.unidad.nombre)
    estatus_solicitud = db().select(db.estatus_solicitud.ALL, orderby=db.estatus_solicitud.nombre_estatus)
    prioridad = db().select(db.prioridad.ALL, orderby=db.prioridad.nombre_prioridad)
    espacio = db().select(db.espacio.ALL, orderby=db.espacio.nombre_espacio)
    lugar = db().select(db.lugar.ALL, orderby=db.lugar.edificio)
    unidad_metrica = db().select(db.unidad_metrica.ALL, orderby=db.unidad_metrica.nombre_unidadMetrica)
    cod = None

    if request.args(0)!=None:
        cod = request.args(0)

    form_unidadMetrica = SQLFORM(db.unidad_metrica)
    if form_unidadMetrica.accepts(request.vars, session):
        unidad_metrica = db().select(db.unidad_metrica.ALL, orderby=db.unidad_metrica.nombre_unidadMetrica)
        cod = "tabla_unidadMetrica"

    form_edificio = SQLFORM(db.edificio)
    if form_edificio.accepts(request.vars, session):
        edificio = db().select(db.edificio.ALL, orderby=db.edificio.nombre)
        cod = "tabla_edificio"

    form_area = SQLFORM(db.area)
    if form_area.accepts(request.vars, session):
        area = db().select(db.area.ALL, orderby=db.area.nombre)
        cod = "tabla_area"

    form_unidad = SQLFORM(db.unidad)
    if form_unidad.accepts(request.vars, session):
        unidad = db().select(db.unidad.ALL, orderby=db.unidad.nombre)
        cod = "tabla_unidades"

    form_estatus = SQLFORM(db.estatus_solicitud)
    if form_estatus.accepts(request.vars, session):
        estatus_solicitud = db().select(db.estatus_solicitud.ALL, orderby=db.estatus_solicitud.nombre_estatus)
        cod = "tabla_estatusSolicitud"

    form_prioridad = SQLFORM(db.prioridad)
    if form_prioridad.accepts(request.vars, session):
        prioridad = db().select(db.prioridad.ALL, orderby=db.prioridad.nombre_prioridad)
        cod = "tabla_prioridad"

    form_espacio = SQLFORM(db.espacio)
    if form_espacio.accepts(request.vars, session):
        espacio = db().select(db.espacio.ALL, orderby=db.espacio.nombre_espacio)
        cod = "tabla_espacio"

    form_lugar = SQLFORM(db.lugar)
    if form_lugar.accepts(request.vars, session):
        lugar = db().select(db.lugar.ALL, orderby=db.lugar.edificio)
        cod = "tabla_lugar"

    return dict(personal=personal,edificio=edificio,inventario=inventario,area=area,supervisor=supervisor,unidad=unidad,estatus_solicitud=estatus_solicitud,prioridad=prioridad,espacio=espacio,form_edificio = form_edificio,form_area = form_area,form_unidad = form_unidad,form_estatus = form_estatus,form_prioridad = form_prioridad,lugar = lugar,form_lugar=form_lugar,unidad_metrica = unidad_metrica,form_unidadMetrica = form_unidadMetrica, cod = cod)

def eliminar():
    if (request.args(1)=='lugar'):
        db(db.lugar.id==request.args(0)).delete()
        cod = "tabla_lugar"

    elif (request.args(1)=='edificio'):
        db(db.edificio.id==request.args(0)).delete()
        cod = "tabla_edificio"

    elif (request.args(1)=='area'):
        db(db.area.id==request.args(0)).delete()
        cod = "tabla_area"

    elif (request.args(1)=='unidad'):
        db(db.unidad.id==request.args(0)).delete()
        cod = "tabla_unidades"

    elif (request.args(1)=='estatus'):
        db(db.estatus_solicitud.id==request.args(0)).delete()
        cod = "tabla_estatusSolicitud"

    elif (request.args(1)=='prioridad'):
        db(db.prioridad.id==request.args(0)).delete()
        cod = "tabla_prioridad"

    elif (request.args(1)=='unidad_metrica'):
        db(db.unidad_metrica.id==request.args(0)).delete()
        cod = "tabla_unidadMetrica"


    redirect(URL('catalogue',args=cod))
    return dict(cod = cod)

def mod_catalogo():
    if (request.args(1)=='lugar'):
        record = db.lugar(request.args(0))
        form = SQLFORM(db.lugar, record)
        if form.process().accepted:
            response.flash = T('El Lugar fue modificado exitosamente!')
        else:
            response.flash = T('Por favor llene la forma.')
        title = "Lugar"
        cod = "tabla_lugar"
    elif (request.args(1)=='edificio'):
        record = db.edificio(request.args(0))
        form = SQLFORM(db.edificio, record)
        if form.process().accepted:
            response.flash = T('El Edificio fue modificado exitosamente!')
        else:
            response.flash = T('Por favor llene la forma.')
        title = "Edificio"
        cod = "tabla_edificio"
    elif (request.args(1)=='area'):
        record = db.area(request.args(0))
        form = SQLFORM(db.area, record)
        if form.process().accepted:
            response.flash = T('El Área de Trabajo fue modificado exitosamente!')
        else:
            response.flash = T('Por favor llene la forma.')
        title = "Área de Trabajo"
        cod = "tabla_area"
    elif (request.args(1)=='unidad'):
        record = db.unidad(request.args(0))
        form = SQLFORM(db.unidad, record)
        if form.process().accepted:
            response.flash = T('La Unidad fue modificada exitosamente!')
        else:
            response.flash = T('Por favor llene la forma.')
        title = "Unidad"
        cod = "tabla_unidades"
    elif (request.args(1)=='estatus'):
        record = db.estatus_solicitud(request.args(0))
        form = SQLFORM(db.estatus_solicitud, record)
        if form.process().accepted:
            response.flash = T('El Estado de la Solicitud fue modificado exitosamente!')
        else:
            response.flash = T('Por favor llene la forma.')
        title = "Estado de la Solicitud"
        cod = "tabla_estatusSolicitud"
    elif (request.args(1)=='prioridad'):
        record = db.prioridad(request.args(0))
        form = SQLFORM(db.prioridad, record)
        if form.process().accepted:
            response.flash = 'La Prioridad fue modificada exitosamente!'
        else:
            response.flash = T('Por favor llene la forma.')
        title = "Prioridad"
        cod = "tabla_prioridad"
    elif (request.args(1)=='unidad_metrica'):
        record = db.unidad_metrica(request.args(0))
        form = SQLFORM(db.unidad_metrica, record)
        if form.process().accepted:
            response.flash = T('La Unidad Métrica fue modificada exitosamente!')
        else:
            response.flash = T('Por favor llene la forma.')
        title = "Unidad Métrica"
        cod = "tabla_unidadMetrica"
    return locals()

@auth.requires_login()
def inventory():
    return dict()

@auth.requires_login()
def sb():
    return dict()

def error():
    return dict()

'''<!--       <div class="collapse navbar-collapse navbar-ex1-collapse">
          <ul class="nav navbar-nav navbar-right">
            {{='auth' in globals() and auth.navbar('Welcome',mode='dropdown') or ''}}
          </ul>
       </div> -->'''
