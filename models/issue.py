from odoo import fields, models, api, exceptions


class Issue(models.Model):
    _name = "pt.issue"
    _description = "Issue"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Name", required=True, tracking=True)
    description = fields.Text(string="Description", tracking=True)
    weight = fields.Float(string='Weight', default=1.0, tracking=True)
    start_date = fields.Date(string='Start Date', tracking=True)
    end_date = fields.Date(string='End Date', tracking=True)
    priority = fields.Selection([
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ], string='Priority', default='medium', required=True, tracking=True)
    status = fields.Selection([
        ('open', 'Open'),
        ('closed', 'Closed'),
    ], string='Status', default='open', required=True, tracking=True)
    assignee_id = fields.Many2one('res.users', string='Assignee', tracking=True)
    reviewer_id = fields.Many2one('res.users', string='Reviewer', tracking=True)
    project_id = fields.Many2one("pt.project", string="Project", ondelete="cascade")
    label_ids = fields.Many2many('pt.project.label',
                                 string='Tags', group_expand='_group_expand_labels', tracking=True)
    milestone_id = fields.Many2one('pt.project.milestone', string='Milestone', tracking=True)

    @api.model
    def _group_expand_labels(self, statuses, domain, order):
        project_id = self.env.context.get('default_project_id')
        if project_id:
            return (self.env['pt.project.label'].search([
                ('project_id', '=', project_id),
                ('visible', '=', True)],
                order='order asc'))
        else:
            raise ValueError('default_project_id is not set')

    @api.constrains('weight')
    def _check_weight(self):
        for record in self:
            if record.weight < 1:
                raise exceptions.ValidationError('The weight must be at least 1.')

