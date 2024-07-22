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
    issue_ids = fields.One2many('pt.issue', 'project_id', string='Issues')
    issue_tag_ids = fields.One2many('pt.project.issue.tag', 'project_id', string='Issues Tags')
