# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class CalculoRetenciones(models.Model):
    _name = 'calculo.retenciones'
    _description = 'Cálculo de Retenciones'

    empleado_id = fields.Many2one('empleados.empleado', string='Empleado', required=True)
    fecha_calculo = fields.Date(string='Fecha de Cálculo', required=True, default=fields.Date.today)
    salario_base = fields.Float(string='Salario Base', related='empleado_id.Salario', readonly=True, store=True)
    porcentaje_ss = fields.Float(string='Porcentaje Seguridad Social (%)', default=6.35)
    retencion_ss = fields.Float(string='Retención Seguridad Social', compute='_compute_retencion', store=True)
    salario_neto = fields.Float(string='Salario Neto', compute='_compute_salario_neto', store=True)

    @api.depends('salario_base', 'porcentaje_ss')
    def _compute_retencion(self):
        for record in self:
            record.retencion_ss = record.salario_base * (record.porcentaje_ss / 100)

    @api.depends('salario_base', 'retencion_ss')
    def _compute_salario_neto(self):
        for record in self:
            record.salario_neto = record.salario_base - record.retencion_ss 