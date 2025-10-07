
from num2words import num2words
from win32comext.shell.shellcon import FOLDERID_RecordedCalls

from odoo import models, fields, api
class InvoiceH(models.Model):
    _name = "invoice_h"
    _description = "Cash Sale"
    _inherit = ["mail.thread", "mail.activity.mixin"]


    doc_no = fields.Char(
        default='New',
        required=1
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

    gross_total = fields.Char(
        string='Total Amount ',
        compute='_compute_totals',
        store=True,
        currency_field='company_currency_id'
    )
    disc_total = fields.Char(
        string='Discount ',
        compute='_compute_totals',
        store=True,
        currency_field='company_currency_id'
    )
    vat_total = fields.Char(
        string='Tax 15%  ',
        compute='_compute_totals',
        store=True,
        currency_field='company_currency_id'
    )
    net_total = fields.Char(
        string='Net Amount ',
        compute='_compute_totals',
        store=True,
        currency_field='company_currency_id'
    )
    amount_to_words = fields.Char(
        string="Amount in Words",
        compute='_compute_amount_to_words'
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

    def _compute_amount_to_words(self):
        for move in self:
            move.amount_to_words = num2words(move.net_total, lang='ar') + " فقط لا غير"

    @api.model
    def create(self, vals):
        res = super(InvoiceH, self).create(vals)
        if res.doc_no =='New':
           res.doc_no = self.env['ir.sequence'].next_by_code('invoice_h')
        return res


    @api.depends('invoice_ids.gross', 'invoice_ids.disc', 'invoice_ids.vat')
    def _compute_totals(self):
        for move in self:
            move.gross_total = sum(line.gross for line in move.invoice_ids)
            move.disc_total = sum(line.disc for line in move.invoice_ids)
            move.vat_total = sum(line.vat for line in move.invoice_ids)
            move.net_total = (sum(line.gross for line in move.invoice_ids) - sum(line.disc for line in move.invoice_ids)
                              + sum(line.vat for line in move.invoice_ids))

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
