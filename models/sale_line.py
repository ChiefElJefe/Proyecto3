from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Sale_line(models.Model):
    _name = 'proyecto3.saleline'
    _description = 'proyecto3.saleline'

    code_id = fields.Many2one('proyecto3.keycode', string="Code", domain="[('selled', '!=', True)]")
    key_code = fields.Char(string="Key code", related="code_id.key_code")
    creation_date = fields.Date(string="Creation Date", related="code_id.creation_date")
    sell_date = fields.Date(string="sell date", related="code_id.sell_date")
    selled = fields.Boolean(string="Selled", related="code_id.selled")
    sello_id = fields.Many2one('proyecto3.codessells', string="Sell")

    @api.onchange('code_id')
    def _key_filter(self):
        used_code_ids = self.sello_id.keycode_ids.mapped('code_id').ids
        domain = [('id', 'not in', used_code_ids)]
        return {'domain': {'code_id': domain}}

    # @api.constrains('sello_id')
    # def _check_duplicate_sello_id(self):
    #     for record in self:
    #         if record.sello_id:
    #             domain = [('sello_id', '=', record.sello_id.id), ('id', '!=', record.id)]
    #             if self.search_count(domain) > 0:
    #                 raise ValidationError("Cannot save the record. Duplicate sello_id found.")
