from odoo import models, fields


class Branches(models.Model):

    _name = "branches"
    _description = "Branches Code"
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

    # :TODO create the reversed field `Many2Many` with `clients` model
    # :TODO create the reversed field `One2Many` with `rents` model