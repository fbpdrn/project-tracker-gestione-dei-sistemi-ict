from odoo import models, fields


class Tag(models.Model):
    _name = 'pt.project.issue.tag'
    _description = 'Project Issue Tag'

    name = fields.Char(string='Name', required=True)
    order = fields.Integer(string='Order', default=0)
    project_id = fields.Many2one('pt.project', string='Project', ondelete='cascade', required=True)
