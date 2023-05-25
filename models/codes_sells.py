from odoo import models, fields, api


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
    keycode_ids = fields.One2many('proyecto3.keycode', 'sell_id')

