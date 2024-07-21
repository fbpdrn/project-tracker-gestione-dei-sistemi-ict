from odoo import fields, models


class Project(models.Model):
    _name = 'pt.project'
    _description = 'Project'

    name = fields.Char(string='Project name', required=True)
    description = fields.Text(string='Description')
    status = fields.Selection([
        ('on_track', 'On Track'),
        ('at_risk', 'At Risk'),
        ('delayed', 'Delayed'),
    ], string='Status', default='on_track')
