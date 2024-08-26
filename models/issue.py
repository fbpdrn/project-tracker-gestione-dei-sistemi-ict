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
        ('in_progress', 'In Progress'),
        ('in_review', 'In Review'),
        ('cancelled', 'Cancelled'),
        ('closed', 'Closed'),
    ], string='Status', default='open', group_expand='_group_expand_status', required=True, tracking=True)
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

    @api.model
    def _group_expand_status(self, statuses, domain, order):
        return [key for key, val in type(self).status.selection]

    @api.constrains('weight')
    def _check_weight(self):
        for record in self:
            if record.weight < 1:
                raise exceptions.ValidationError('The weight must be at least 1.')

    # Override
    def action_set_status_in_progress(self):
        if self.status != 'open' and self.status != 'in_review':
            raise exceptions.UserError("The current status must be 'Open' or 'In Review'.")
        if self.env.user.id not in [self.assignee_id.id, self.reviewer_id.id]:
            raise exceptions.AccessError("Only the assignee or reviewer can set the status to 'In Progress'.")
        return self.sudo().write({'status': 'in_progress'})

    # Override
    def action_set_status_in_review(self):
        if self.status != 'in_progress':
            raise exceptions.UserError("The current status must be 'In Progress'.")
        if self.env.user.id not in [self.assignee_id.id]:
            raise exceptions.AccessError("Only the assignee can set the status to 'In Review'.")
        return self.sudo().write({'status': 'in_review'})

    # Override
    def action_set_status_closed(self):
        if self.status != 'in_review':
            raise exceptions.UserError("The current status must be 'In Review'.")
        if self.env.user.id not in [self.reviewer_id.id]:
            raise exceptions.AccessError("Only the reviewer can set the status to 'Closed'.")
        return self.sudo().write({'status': 'closed'})

    # Override
    def message_post(self, **kwargs):
        return super(Issue, self.sudo()).message_post(**kwargs)

