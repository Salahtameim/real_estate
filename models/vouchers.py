from odoo import models, fields


class vouchers(models.Model):

    _name = "vouchers"
    _description = "Vouchers Entry"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    date = fields.Date(
        string="Date ",
        copy=True,
        required=True
    )
    branches = fields.Many2one(
        comodel_name="branches",
        ondelete="restrict",
        string="Branches Code",
        copy=True,
        required=True
    )

    doc = fields.Char(
        string="Doc NO",
        copy=True,
        required=True
    )
    voline_ids = fields.One2many(
        comodel_name="voucher_line",
        inverse_name="voucher_id",
        string="Line",
        copy=True
    )
    state = fields.Selection(
        selection=[
            ("draft", "Draft"),
            ("cancel", "Cancel")
        ],
        string="State",
        copy=True,
        default="draft"

    )

    def cancel_vouchers(self):
        """
        This method responsible for canceling the travel
        """
        self.state = "cancel"

    def vouchers_completed(self):
        """
        This method complete the travel
        """
        self.state = "post"







