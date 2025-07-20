
from odoo import models, fields
class Inv_h(models.Model):

    _name = "invoice_h"
    _description = "Cash Sale"
    _inherit = ["mail.thread", "mail.activity.mixin"]


    doc_no = fields.Char(
        string="Doc No",
        copy=True,
        required=True
    )
    date = fields.Date(
        string="Date",
        copy=True,
        required=True
    )
    customer = fields.Many2one(
        comodel_name="owners",
        ondelete="restrict",
        string="customer",
        copy=True,
        required=True
    )

    vat = fields.Char(
        string=" Vat No",
        copy=True,
        required=True,
        related="customer.vat"

    )



    invoice_ids = fields.One2many(
        comodel_name="invoice_d",
        inverse_name="invoice_id",
        string="Line",
        copy=True
    )
    state = fields.Selection(
        selection=[
            ("draft", "Draft"),
            ("scheduled", "Scheduled"),
            ("running", "Running"),
            ("end", "Terminated"),
            ("cancel", "Cancel")
        ],
        string="State",
        copy=True,
        default="draft"
    )

    def posting(self):
        """
        This method responsible for scheduling the travel
        """

        self.state = "scheduled"

        return

    def cancel_rent(self):
        """
        This method responsible for launching the travel
        """
        self.state = "cancel"
        return

    def cancel_travel(self):
        """
        This method responsible for canceling the travel
        """
        self.state = "cancel"

    def travel_completed(self):
        """
        This method complete the travel
        """
        self.state = "end"
