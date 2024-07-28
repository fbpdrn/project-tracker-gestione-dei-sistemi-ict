from odoo import models, fields


class Label(models.Model):
    _name = 'pt.project.label'
    _description = 'Project Label'

    name = fields.Char(string='Name', required=True)
    order = fields.Integer(string='Order', default=0, required=True)
    visible = fields.Boolean(string='Visible', default=True, required=True)
    project_id = fields.Many2one('pt.project', string='Project', ondelete='cascade', required=True)
