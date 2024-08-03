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
    assignee_ids = fields.Many2many('res.users', string='Assignees', compute='_compute_assignee_ids', store=True)

    open_issues_count = fields.Integer(string='Open Issues Count', compute='_compute_issues_count', store=True)
    in_progress_issues_count = fields.Integer(string='In Progress Issues Count', compute='_compute_issues_count', store=True)
    in_review_issues_count = fields.Integer(string='In Review Issues Count', compute='_compute_issues_count', store=True)
    cancelled_issues_count = fields.Integer(string='Cancelled Issues Count', compute='_compute_issues_count', store=True)
    closed_issues_count = fields.Integer(string='Closed Issues Count', compute='_compute_issues_count', store=True)
    issues_count = fields.Integer(string='Issues Count', compute='_compute_issues_count', store=True)
    active_issues_count = fields.Integer(string='Active Issues Count', compute='_compute_issues_count', store=True)

    milestones_count = fields.Integer(string='Milestones Count', compute='_compute_milestones_count', store=True)
    active_milestones_count = fields.Integer(string='Active Milestones Count', compute='_compute_milestones_count', store=True)

    @api.depends('issue_ids.status')
    def _compute_issues_count(self):
        for project in self:
            project.open_issues_count = len(project.issue_ids.filtered(lambda issue: issue.status == 'open'))
            project.in_progress_issues_count = len(project.issue_ids.filtered(lambda issue: issue.status == 'in_progress'))
            project.in_review_issues_count = len(project.issue_ids.filtered(lambda issue: issue.status == 'in_review'))
            project.cancelled_issues_count = len(project.issue_ids.filtered(lambda issue: issue.status == 'cancelled'))
            project.closed_issues_count = len(project.issue_ids.filtered(lambda issue: issue.status == 'closed'))
            project.issues_count = len(project.issue_ids)
            project.active_issues_count = project.open_issues_count + project.in_progress_issues_count + project.in_review_issues_count

    @api.depends('milestone_ids.project_id')
    def _compute_milestones_count(self):
        for project in self:
            project.milestones_count = len(project.milestone_ids)
            project.active_milestones_count = len(project.milestone_ids.filtered(lambda milestone: milestone.status == 'open'))

    @api.depends('issue_ids.assignee_id')
    def _compute_assignee_ids(self):
        for project in self:
            assignee_ids = project.issue_ids.mapped('assignee_id').ids
            project.assignee_ids = [(6, 0, assignee_ids)]

    @api.model
    def _group_expand_status(self, statuses, domain, order):
        return [key for key, val in type(self).status.selection]
