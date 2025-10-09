from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Vouchers(models.Model):
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
    name = fields.Char(
        default='New',
        required=1
    )
    voline_ids = fields.One2many(
        comodel_name="voucher_line",
        inverse_name="voucher_id",
        string="Line",
        copy=True
    )
    total_debit = fields.Char(
        string='Total Debit',
        compute='_compute_totals',
        store=True,
        currency_field='company_currency_id'
    )
    total_credit = fields.Char(
        string='Total Credit',
        compute='_compute_totals',
        store=True,
        currency_field='company_currency_id'
    )
    total_difference = fields.Char(
        string='Total Difference',
        compute='_compute_totals',
        store=True,
        currency_field='company_currency_id'
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
    @api.model
    def create(self, vals):
        res = super(Vouchers, self).create(vals)
        if res.name == 'New':
            res.name = self.env['ir.sequence'].next_by_code('vouchers')
        return res

    @api.onchange('voline_ids')
    def _onchange_voline_ids_balance(self):
        if len(self.voline_ids) == 2:
            line1, line2 = self.voline_ids
            if line1.debit:
                line2.credit = line1.debit
            elif line1.credit:
                line2.debit = line1.credit

    @api.depends('voline_ids.debit', 'voline_ids.credit')
    def _compute_totals(self):
        for move in self:
            move.total_debit = sum(line.debit for line in move.voline_ids)
            move.total_credit = sum(line.credit for line in move.voline_ids)
            move.total_difference = (
                        sum(line.debit for line in move.voline_ids) - sum(line.credit for line in move.voline_ids))

    @api.constrains('voline_ids')
    def _check_total_debit_total_credit_difference(self):
        for move in self:
            total_debit = sum(line.debit for line in move.voline_ids)
            total_credit = sum(line.credit for line in move.voline_ids)
            if round(total_debit, 2) != round(total_credit, 2):
                raise ValidationError("لا يمكن حفظ القيد لأن إجمالي المدين لا يساوي إجمالي الدائن.")

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


