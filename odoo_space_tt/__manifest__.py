# -*- coding: utf-8 -*-

{
    'name': 'Odoo Space TT 1',
    
    'summary': """Academy app to manage Odoo Space Program""",

    'description': """
        Academy Module to manage Training:
        - Spaceships and more
        """,
    
    'author': 'Odoo',
    
    'website': 'https://www.odoo.com',
    
    'category': 'Training',
    'version': '0.1',
    
    'depends': ['base'],
    
    'data': [
        'security/spaceship_security.xml',
        'security/ir.model.access.csv',
        'views/spaceship_menu_items.xml',
        'views/spaceship_views.xml',
    ],
    'demo': [
        'demo/spaceship_demo.xml',
    ],
    #Add license to remove License Warning
    'license': 'OPL-1'
}