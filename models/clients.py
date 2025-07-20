from odoo import models, fields


class Clients(models.Model):
    """
    This model holds the client for the Real Estate
    """
    _name = "clients" # real_estate.model_clients
    _description = "Rent Contract"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(
        string="Name",
        copy=True,
        required=True
    )

    # Bad implementation
    # :TODO the field `branch` should be named `branches`
    # :TODO the field `branch` should be `Many2Many` field with model `branches`

    branch = fields.Integer(
        string="Branch",
        copy=True,
        default=1

    )
