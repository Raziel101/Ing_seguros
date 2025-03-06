# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import datetime
from odoo.exceptions import Warning
from dateutil.relativedelta import relativedelta
import logging
_logger = logging.getLogger(__name__)


class plantilla_iasper(models.Model):
    _name = 'ing.seguros.planilla.iasper'
    _inherit = 'ing.seguros.planilla.art'
    _description = 'Denuncia de Accidente'

    # Datos del siniestro
    poliza_numero = fields.Char(string="Póliza N°")
    siniestro_numero = fields.Char(string="Siniestro N°")
    tomador_nombre = fields.Char(string="Tomador Nombre")
    telefono_denunciante = fields.Char(string="Teléfono Denunciante")
    lugar_fecha = fields.Text(string="Lugar y Fecha")
    nota = fields.Text(string="Nota",default="Este formulario debe remitirse junto con el INFORME MÉDICO, inmediatamente de producido el siniestro.")

    # Datos del denunciante
    calle = fields.Char(string="Calle")
    numero = fields.Char(string="N°")
    localidad = fields.Char(string="Localidad")
    dpto = fields.Char(string="Dpto")
    email_denunciante = fields.Char(string="E-mail Denunciante")

    # Datos del asegurado
    employee_id = fields.Many2one('hr.employee', string='Empleado', required=True, domain='[("tipo_contrato_id","in",["Locación de Servicios","locacion de servicios"])]')
    asegurado_nombre = fields.Char(string="Apellido y Nombre del Asegurado")
    asegurado_dni = fields.Char(string="DNI del Asegurado")
    asegurado_email = fields.Char(string="E-mail Asegurado")
    asegurado_calle = fields.Char(string="Calle Asegurado")
    asegurado_provincia = fields.Char(string="Provincia")
    asegurado_cp = fields.Char(string="C.P")
    asegurado_edad = fields.Integer('Edad', compute='_calcule_edad', store=False, required=True)
    asegurado_localidad = fields.Char(string="Localidad")
    asegurado_numero = fields.Char(string="N°")
    asegurado_piso = fields.Char(string="Piso")
    asegurado_dpto = fields.Char(string="Dpto")
    tarea_efectuada = fields.Char(string="Tarea que efectúa")

    # Datos del Beneficiario
    beneficiario_nombre = fields.Char(string="Apellido y Nombre del Beneficiario")
    cuenta_obra_social = fields.Boolean(string="¿Cuenta con Obra Social?")
    especificar_obra_social = fields.Char(string="Especificar")

    # Circunstancias del accidente
    dia = fields.Integer(string="Día")
    mes = fields.Integer(string="Mes")
    anio = fields.Integer(string="Año")
    hora = fields.Char(string="Hora")
    lugar_accidente = fields.Text(string="Lugar donde ocurrió")
    circunstancias = fields.Text(string="Circunstancias en que se produjo (explicar detalladamente)")
    actividad_accidentado = fields.Text(string="Actividad que efectuaba el accidentado en aquel momento")
    parte_cuerpo_lesionado = fields.Char(string="Parte del cuerpo lesionado")
    tipo_lesion = fields.Char(string="Tipo de lesión")
    medico_primera_atencion = fields.Char(string="Nombre del médico o establecimiento transitorio que prestó primeros auxilios")

    # Testigos y denuncia
    hubo_testigos = fields.Boolean(string="¿Hubo testigos del accidente?")
    nombres_testigos = fields.Text(string="Nombres y Apellidos testigos")
    domicilios_testigos = fields.Text(string="Domicilios testigo")
    sumario_policial = fields.Boolean(string="¿Se instruyó sumario policial?")
    autoridad = fields.Char(string="¿A qué autoridad fue elevado? (si es juez indíquese también Secretaría)")

    # Datos del denunciante
    tipo_denunciante = fields.Selection([
        ('empleador', 'Empleador'),
        ('representante', 'Representantes Legales'),
        ('beneficiario', 'Beneficiarios'),
        ('otro', 'Otro')
    ], string="¿Quién es el denunciante?")

    denunciante_nombre = fields.Char(string="Apellido y Nombre denunciante")
    denunciante_domicilio = fields.Char(string="Domicilio del Denunciante")



    def _calcule_edad(self):
        self.asegurado_edad = relativedelta(datetime.now(), self.employee_id.birthday).years

    def name_get(self):
        return [(record.id, str(record.employee_id.name) + '-' + str(record.date_accident)) for record in self]

