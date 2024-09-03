from odoo import fields, models, api, exceptions


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

    @api.constrains('start_date', 'end_date')
    def _check_dates(self):
        for record in self:
            if record.end_date and record.start_date and record.end_date < record.start_date:
                raise exceptions.ValidationError('Milestone: the end date must be greater than or equal to the start date.')