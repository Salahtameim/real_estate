from odoo import models, fields


class Branches(models.Model):

    _name = "bank"
    _description = "Bank Name"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    code = fields.Char(
        string="code",
        copy=True,
        required=True
    )

    name = fields.Char(
        string="Name",
        copy=True,
        required=True
    )

