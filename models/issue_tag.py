from odoo import models, fields


class Tag(models.Model):
    _name = 'pt.project.issue.tag'
    _description = 'Project Issue Tag'

    name = fields.Char(string='Name', required=True)
    color = fields.Char(string='Color', help='Background color', required=True)
    project_id = fields.Many2one('pt.project', string='Project', ondelete='cascade', required=True)
