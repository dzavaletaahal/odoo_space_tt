# .*. coding: utf-8 -*-

from odoo import models, fields, api
from datetime import timedelta

class Mission(models.Model):
    _name = 'mission'
    _description = 'Mission Info'

    spaceship_id = fields.Many2one(comodel_name='spaceship',
                               string='Spaceship',
                               ondelete='cascade',
                               required=True)

    assigned_spaceship = fields.Char(string='Assigned spaceship', related='spaceship_id.name')
    
    launch_date = fields.Date(string="Launch date")
    
    return_date = fields.Date(string="Return date")

    crew_members = fields.Many2many(comodel_name='res.partner', string='Crew members')