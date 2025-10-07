from odoo import models, fields,api
class InvoiceD(models.Model):
    _name = "invoice_d"
    _description = "Cash Sale Item"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    item_code = fields.Char(
        string="Item Code",
        copy=True,
        required=True,
        related="item_id.code"
    )
    item_id = fields.Many2one(
        comodel_name="items",
        ondelete="restrict",
        string="Item Name",
        copy=True,
        required=True

    )
    qty = fields.Float(
        string="Qty",
        copy=True,
        required=True
    )
    price = fields.Float(
        string="Price",
        copy=True,
        required=True
    )
    gross = fields.Float(
        string="G.Total",
        compute='_compute_gross',
        store=True
    )
    disc = fields.Float(
        string="Disc",
        copy=True,
        required=True
    )
    vat = fields.Float(
        string="Vat 15%",
        compute='_compute_vat',
        store=True
    )
    total = fields.Float(
        string="Total amount",
        compute = '_compute_total',
        store = True
    )

    invoice_id = fields.Many2one(
        comodel_name="invoice_h",
        ondelete="restrict",
        string="Related real estate",
        copy=True,
        required=True
    )
    @api.depends('qty', 'price')
    def _compute_gross(self):
        for record in self:
            record.gross = record.qty * record.price

    @api.depends('qty', 'price', 'disc', 'vat')
    def _compute_vat(self):
        for record in self:
            record.vat = (record.qty * record.price - record.disc) * 0.15


    @api.depends('qty', 'price', 'disc')
    def _compute_total(self):
        for record in self:
            record.total = record.gross - record.disc + record.vat


