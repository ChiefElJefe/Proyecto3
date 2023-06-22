from odoo import models, fields, api


class Invoice_line(models.Model):
    _name = 'proyecto3.invoiceline'
    _description = 'proyecto3.invoiceline'

    code_id = fields.Many2one('proyecto3.keycode', string="Code")
    key_code = fields.Char(string="Key code", related="code_id.key_code")
    creation_date = fields.Date(string="Creation Date", related="code_id.creation_date")
    sell_date = fields.Date(string="sell date", related="code_id.sell_date")
    selled = fields.Boolean(string="Selled", related="code_id.selled")
    invoice_id = fields.Many2one('proyecto3.invoicesells', string="Invoice")

    @api.onchange('code_id')
    def key_filter(self):
        used_code_ids = self.invoice_id.keycode_ids.mapped('code_id').ids
        domain = [('id', 'not in', used_code_ids), ('selled', '!=', True)]
        return {'domain': {'code_id': domain}}
