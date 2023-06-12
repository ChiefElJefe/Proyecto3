from odoo import models, fields, api


class Key_code(models.Model):
    _name = 'proyecto3.keycode'
    _description = 'proyecto3.keycode'

    name = fields.Char(string="Product")
    key_code = fields.Char(string="Key code")
    creation_date = fields.Date(string="Creation Date", default=fields.Date.context_today)
    sell_date = fields.Date(string="sell date")
    selled = fields.Boolean(string="Selled")
    list_price = fields.Float(string="Cost Price")
    tax_id = fields.Many2one('account.tax', string="Tax")
    standard_price = fields.Float(string="Sale Price")
    # sell_id = fields.Many2one('proyecto3.codessells', string="Sell")

    # def code_generator(self):
    #     existe = True
    #     while existe:
    #         codes = '-'.join([''.join(random.choices(string.ascii_uppercase + string.digits, k=5)) for i in range(3)])
    #         search_codes = self.env['proyecto3.keycode'].search([('key_code', '=', codes)])
    #         if not search_codes:
    #             existe = False
    #             print(codes)
    #             return codes
    #
    # def create_codes(self):
    #     for i in range(50):
    #         new_record = self.create({
    #             'name': 'Game1',
    #             'key_code': self.code_generator()
    #         })
    #
    #     return True
