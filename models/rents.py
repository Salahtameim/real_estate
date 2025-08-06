from odoo import models, fields

class Rents(models.Model):
    _name = "rents"
    _description = "Rent contract"
    _inherit = ["mail.thread",  "mail.activity.mixin"]


    owner = fields.Many2one(
        comodel_name="owners",
        ondelete="restrict",
        string="Owners",
        copy=True,
        required=True
    )

    property = fields.Many2one(
        comodel_name="types",
        ondelete="restrict",
        string="Property Type",
        copy=True,
        required=True
    )

    contract = fields.Char(
        string="Contract No",
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

    amount = fields.Float(
        string="Rent Amount",
        copy=True,
        required=True
    )

    # Everything should be with the same language
    payment =  fields.Selection(
            selection=[
                ("draft", "كل_عام"),
                ("scheduled", "نصف_عام")

            ],
                 string="payment",
                 copy=True,
                 default="draft"
    )

    start = fields.Date(
        string="From Date ",
        copy=True,
        required=True
    )

    # :TODO (later) `end` should be tested if its greater than `start` (decorated method `@api.onchange`)

    end  = fields.Date(
        string="End Date ",
        copy=True,
        required=True
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
