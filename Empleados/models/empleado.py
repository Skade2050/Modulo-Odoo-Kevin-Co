# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Empleado(models.Model):
    _name = 'empleados.empleado'
    _description = 'Empleado'

    Nombre = fields.Text(string='Nombre', required=True)
    Apellido = fields.Text(string='Apellido', required=True)
    Puesto = fields.Text(string='Puesto', required=True)
    Edad = fields.Integer(string='Edad', required=True)
    Salario = fields.Float(string='Salario', required=True)

    def name_get(self):
        result = []
        for record in self:
            name = f"{record.Nombre} {record.Apellido}"
            result.append((record.id, name))
        return result
