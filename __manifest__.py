# -*- coding: utf-8 -*-
{

    'name': "Real Estate",

    'summary': "Real Estate management",

    'description': """
    Real Estate management created by  Salah'
    """,

    'author': 'Salah',

    'category': 'Sales/Sales',
    'version': '0.1',

    'depends': ['base', 'sale'],

    'data': [
        'security/res_groups.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'report/qweb_testing.xml',
        'report/qweb_testing3.xml',
        'report/qweb_voucher_rp.xml',
        'views/report.xml',
        'views/report3.xml',
        'views/voucher_report.xml'
    ],

    "application": True
}
