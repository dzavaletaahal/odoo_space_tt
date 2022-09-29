# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class Spaceship(models.Model):
    
    _name = 'spaceship'
    _description = 'Spaceship Info'

    name = fields.Char(string='Spaceship name', required=True)
    ship_dimensions = fields.Char(string='Dimensions')
    ship_lenght = fields.Integer()
    ship_width = fields.Integer()
    ship_type = fields.Char(string='Ship Type')
    num_passengers = fields.Integer(string='Number of passengers')
    fuel_type = fields.Char(string='Type of fuel')
    active = fields.Boolean(string="Active")
    
    
    @api.constrains('ship_lenght','ship_width')
    def _check_additional_fee(self):
        for record in self:
            if record.ship_width > record.ship_lenght:
                raise ValidationError(_('Width can not be bigger than lenght' )) 
    
    mission_ids = fields.One2many(comodel_name='mission',
                                  inverse_name='spaceship_id', 
                                  string='Missions')