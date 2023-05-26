from odoo import models, fields, api


class Sale_line(models.Model):
    _name = 'proyecto3.saleline'
    _description = 'proyecto3.saleline'

    code_id = fields.Many2one('proyecto3.keycode', string="Code")
    key_code = fields.Char(string="Key code", related="code_id.key_code")
    creation_date = fields.Date(string="Creation Date", related="code_id.creation_date")
    sell_date = fields.Date(string="sell date", related="code_id.sell_date")
    used = fields.Boolean(string="Used", related="code_id.used")
    sello_id = fields.Many2one('proyecto3.codessells', string="Sell")
