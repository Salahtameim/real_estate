from odoo import models, fields,api
class VoucherLine(models.Model):

    _name = "voucher_line"
    _description = "Voucher Data"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    bank_id = fields.Many2one(
        comodel_name="bank",
        ondelete="restrict",
        string="Acc name",
        copy=True,
        required=True
    )
    acc_code = fields.Char(
        string="Acc code",
        copy=True,
        required=True,
        related="bank_id.code"
    )
    dimension = fields.Many2one(
        comodel_name="branches",
        ondelete="restrict",
        string="Dimension",
        copy=True,
        required=True
    )
    description = fields.Char(
        string="Description",
        copy=True,
        required=True
    )
    sub_acc = fields.Char(
        string="Sub Acc",
        copy=True,
        required=True,
    )
    debit = fields.Float(
        string="Debit",
        copy=True,
        required=True
    )
    credit = fields.Float(
        string="Credit",
        copy=True,
        required=True
    )
    voucher_id = fields.Many2one(
        comodel_name="vouchers",
        ondelete="restrict",
        string="Related real estate",
        copy=True,
        required=True
    )

    @api.onchange('debit')
    def _onchange_debit(self):
        for line in self:
            if line.debit > 0.0:
                line.credit = 0.0

