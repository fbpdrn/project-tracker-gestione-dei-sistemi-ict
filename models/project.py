from odoo import fields, models, api


class Project(models.Model):
    _name = 'pt.project'
    _description = 'Project'

    name = fields.Char(string='Project name', required=True)
    description = fields.Text(string='Description')
    status = fields.Selection([
        ('on_track', 'On Track'),
        ('at_risk', 'At Risk'),
        ('delayed', 'Delayed'),
    ], string='Status', default='on_track', group_expand='_group_expand_status')
    issue_ids = fields.One2many('pt.issue', 'project_id', string='Issues')
    milestone_ids = fields.One2many('pt.project.milestone', 'project_id', string='Milestones')
    labels_ids = fields.One2many('pt.project.label', 'project_id', string='Labels')
    open_issues_count = fields.Integer(string='Open Issues Count', compute='_compute_open_issues_count')
    assignee_ids = fields.Many2many('res.users', string='Assignees', compute='_compute_assignee_ids', store=True)

    @api.depends('issue_ids.status')
    def _compute_open_issues_count(self):
        for project in self:
            project.open_issues_count = len(project.issue_ids.filtered(lambda issue: issue.status == 'open'))

    @api.depends('issue_ids.assignee_id')
    def _compute_assignee_ids(self):
        for project in self:
            assignee_ids = project.issue_ids.mapped('assignee_id').ids
            project.assignee_ids = [(6, 0, assignee_ids)]

    @api.model
    def _group_expand_status(self, statuses, domain, order):
        return [key for key, val in type(self).status.selection]
