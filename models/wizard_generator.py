from odoo import models, fields, api
from odoo.exceptions import UserError
import random
import string


class Wizard_generator(models.TransientModel):
    _name = 'proyecto3.wizardgenerator'
    _description = 'proyecto3.wizardgenerator'

    name = fields.Char(string="Product name")
    list_price = fields.Float(string="Cost Price")
    tax_id = fields.Many2one('account.tax', string="Tax")

    def code_generator(self):
        existe = True
        while existe:
            codes = '-'.join([''.join(random.choices(string.ascii_uppercase + string.digits, k=5)) for i in range(3)])
            search_codes = self.env['proyecto3.keycode'].search([('key_code', '=', codes)])
            if not search_codes:
                existe = False
                # print(codes)
                return codes

    def tax_cal(self):
        for rec in self:
            tax_percent = rec.tax_id.amount / 100
            price_calc = rec.list_price + (rec.list_price * tax_percent)
            return price_calc

    def create_codes(self):
        if not self.name:
            raise UserError('The product name field is empty')
            return True
        else:
            for i in range(50):
                new_record = self.env['proyecto3.keycode'].create({
                    'name': self.name,
                    'list_price': self.list_price,
                    'key_code': self.code_generator(),
                    'tax_id': self.tax_id.id,
                    'standard_price': self.tax_cal(),
                })

            return {
                'type': 'ir.actions.client',
                'tag': 'reload',
            }
