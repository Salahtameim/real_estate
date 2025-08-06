from odoo import models, fields


class SubAcc(models.Model):

    _name = "sub_acc"
    _description = "Sub account"
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(
        string="Name",
        copy=True,
        required=True
    )

    code = fields.Char(
        string="code",
        copy=True,
        required=True
    )

    acc = fields.Many2one(
        comodel_name="bank",
        ondelete="restrict",
        string="control Acc",
        copy=True,
        required=True
    )
