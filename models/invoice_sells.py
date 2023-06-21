from odoo import models, fields, api

pay_form = [
    ('credit', 'Credit Card'), ('paypar', 'Paypar')
]


class Invoice_sells(models.Model):
    _name = 'proyecto3.invoicesells'
    _description = 'proyecto3.invoicesells'

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
    currency_id = fields.Many2one('res.currency', string="Coin", required=True)
    keycode_ids = fields.One2many('proyecto3.saleline', 'sello_id', required=True)
    pay_count = fields.Char(string="Count")
    card_name = fields.Char(string="Card name")
    card_number = fields.Integer(string="Card number")
    card_ex_month = fields.Char(string="Expiration Date Month")
    card_ex_year = fields.Char(string="Expiration Date Year")
    cvv = fields.Integer(string="CVV")
    type_pay = fields.Selection(pay_form, string="Type pay", default='paypar')
    total_sum = fields.Float(string="Total:")
    in_tax_sum = fields.Float(string="Base:")
    tax_sum = fields.Float(string="Tax:")
    sell_id = fields.Many2one('proyecto3.codessells')
