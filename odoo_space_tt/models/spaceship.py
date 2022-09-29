# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class Spaceship(models.Model):
    
    _name = 'spaceship'
    _description = 'Spaceship Info'

    name = fields.Char(string='Spaceship name', required=True)
    ship_dimensions = fields.Char(string='Dimensions')
    ship_type = fields.Char(string='Ship Type')
    num_passengers = fields.Integer(string='Number of passengers')
    fuel_type = fields.Char(string='Type of fuel')
    active = fields.Boolean(string="Active")
    