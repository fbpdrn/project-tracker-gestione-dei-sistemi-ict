{
    'name': 'Project Tracker',
    'version': '1.0',
    'depends': ['base'],
    'author': 'Fabio Pedrini',
    'category': 'Uncategorized',
    'license': 'LGPL-3',
    'description': """
        Assignment Gestione dei Sistemi ICT 2023/2024
    """,
    'data': [
        'views/project_view.xml',
        'views/issue_view.xml',
        'views/issue_tag_view.xml',
        'views/milestone_view.xml',
        'views/menu.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [],
    'assets': {
        'web.assets_backend': [
            'project-tracker/static/src/css/kanban_style.css',
        ],
    },
    'application': True

}