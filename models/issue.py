from odoo import fields, models


class Issue(models.Model):
    _name = "pt.issue"
    _description = "Issue"

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
    weight = fields.Float(string='Weight')
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
    priority = fields.Selection([
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ], string='Priority', default='medium')
    assignee_id = fields.Many2one('res.users', string='Assignee')
    reviewer_id = fields.Many2one('res.users', string='Reviewer')
    project_id = fields.Many2one("pt.project", string="Project", ondelete="cascade")
    tag_ids = fields.Many2many('pt.project.issue.tag', string='Tags', ondelete="restrict")
    milestone_id = fields.Many2one('pt.project.milestone', string='Milestone')
