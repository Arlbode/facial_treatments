{
    'name': 'Tratamientos Faciales',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Gestión de tratamientos faciales por cliente',
    'description': 'Registra historial de tratamientos, productos usados y próximas citas.',
    'author': 'VitalSkin',
    'depends': ['sale', 'product', 'calendar'],
    'data': [
        'security/ir.model.access.csv',
        'data/facial_treatment_data.xml',
        'views/facial_treatment_views.xml',
        'views/res_partner_views.xml',
    ],
    'installable': True,
    'application': True,
}