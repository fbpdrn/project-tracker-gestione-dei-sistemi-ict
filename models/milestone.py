from odoo import models, fields


class Milestone(models.Model):
    _name = 'pt.project.milestone'
    _description = 'Project Milestone'

    name = fields.Char(string='Name', required=True)
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
    status = fields.Selection([
        ('open', 'Open'),
        ('closed', 'Closed'),
    ], string='Status', default='open')
    project_id = fields.Many2one('pt.project', string='Project', ondelete='cascade', required=True)
