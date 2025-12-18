{
    'name': 'Digizilla',
    'version': '1.0',
    'category': 'Custom',
    'summary': 'Digizilla Module',
    'description': 'Manage Digizilla records with custom fields, views, and reports.',
    'author': 'Your Name',
    'depends': ['base', 'contacts'],
    'data': [
        'views/digizilla_views.xml',
        'reports/digizilla_report.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'digizilla/static/src/js/hide_create_button.js',
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
}
