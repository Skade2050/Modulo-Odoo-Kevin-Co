# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Trabajadores(models.Model):
    _name = 'trabajadores'
    _description = 'Trabajadores'

    Nombre = fields.Text(string='Nombre', required=True)
    Apellidos = fields.Char(string='Apellido', required=True)
    Puesto = fields.Char(string='Puesto', required=True)
    Salario = fields.Char(string='Salario', required=True)
