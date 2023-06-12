from datetime import datetime

from odoo import models, fields, api
from odoo.exceptions import ValidationError

pay_form = [
    ('credit', 'Credit Card'), ('paypar', 'Paypar')
]


class Codes_sells(models.Model):
    _name = 'proyecto3.codessells'
    _description = 'proyecto3.codessells'

    name = fields.Char(string="Name", required=True)
    first_lastname = fields.Char(string="First lastname")
    second_lastname = fields.Char(string="Second lastname")
    email = fields.Char(string="Email", required=True)
    sell_date = fields.Date(string="Sell Date", default=fields.Date.context_today)
    street = fields.Char(string="Street")
    portal = fields.Integer(string="Portal")
    door = fields.Integer(string="Door")
    mobilphone = fields.Integer(string="Mobilphone")
    city = fields.Char(string="City")
    country_id = fields.Many2one('res.country', string="Country")
    province_id = fields.Many2one('res.country.state', string="Province")
    zip = fields.Char(string="C.P.")
    currency_id = fields.Many2one('res.currency', string="Country", required=True)
    keycode_ids = fields.One2many('proyecto3.saleline', 'sello_id', required=True)
    pay_count = fields.Char(string="Count")
    card_name = fields.Char(string="Card name")
    card_number = fields.Integer(string="Card number")
    card_ex_month = fields.Char(string="Expiration Date Month")
    card_ex_year = fields.Char(string="Expiration Date Year")
    cvv = fields.Integer(string="CVV")
    type_pay = fields.Selection(pay_form, string="Type pay", default='paypar')

    @api.model
    def create(self, vals):
        record = super(Codes_sells, self).create(vals)
        record.keycode_ids.code_id.write({'selled': True})
        return record

    def write(self, vals):
        for record in self:
            print(record.keycode_ids)
            record.keycode_ids.code_id.write({'selled': True})
        return super(Codes_sells, self).write(vals)
