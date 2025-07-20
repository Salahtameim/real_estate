from odoo import models, fields


class Types(models.Model):

    _name = "types"
    _description = "Property types"
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

    # :TODO Create the reversed `One2Many` field named `rents` with model `rents`