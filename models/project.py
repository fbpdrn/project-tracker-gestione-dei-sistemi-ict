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
    issue_tag_ids = fields.One2many('pt.project.issue.tag', 'project_id', string='Issues Tags')
    open_issues_count = fields.Integer(string='Open Issues Count', compute='_compute_open_issues_count')

    @api.depends('issue_ids.status')
    def _compute_open_issues_count(self):
        for project in self:
            project.open_issues_count = len(project.issue_ids.filtered(lambda issue: issue.status == 'open'))

    @api.model
    def _group_expand_status(self, statuses, domain, order):
        return [key for key, val in type(self).status.selection]

