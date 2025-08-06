from odoo import models, fields

class Owners(models.Model):

    _name = "owners"
    _description = "Property Owners"
    _inherit = ["mail.thread", "mail.activity.mixin"]


    name = fields.Char(
        string="Name",
        copy=True,
        required=True
    )

    nationality = fields.Char(
        string="Nationality",
        copy=True,
        required=True
    )

    """
     - Never use the `id` field in any model, because of Odoo generate and manage it automatically.
     - For order use case the field `create_date` can be an alternative.
     - For the best use case we create a field with different name such as `sequence` and use it for the order.
     Conclusion: the field `id` must be removed completely.
    """

    id = fields.Char(
        string=" Id No",
        copy=True,
        required=True
    )

    deed_no = fields.Char(
        string=" Deed No",
        copy=True,
        required=True
    )

    vat = fields.Char(
        string=" Vat No",
        copy=True,
        required=True
    )

    email = fields.Char(
        string=" Email",
        copy=True,
        required=True
    )

    address = fields.Char(
        string=" National Address",
        copy=True,
        required=True
    )

    state = fields.Selection(
        selection=[
            ("draft", "Draft")
        ],
        string="State",
        copy=True,
        default="draft"

    )
