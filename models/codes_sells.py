from odoo import models, fields, api

pay_form = [
    ('credit', 'Credit Card'), ('paypar', 'Paypar')
]

state_form = [
    ('draft', 'Draft'), ('invoiced', 'Invoiced')
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
    currency_id = fields.Many2one('res.currency', string="Coin", required=True)
    keycode_ids = fields.One2many('proyecto3.saleline', 'sello_id', required=True)
    pay_count = fields.Char(string="Count")
    card_name = fields.Char(string="Card name")
    card_number = fields.Integer(string="Card number")
    card_ex_month = fields.Char(string="Expiration Date Month")
    card_ex_year = fields.Char(string="Expiration Date Year")
    cvv = fields.Integer(string="CVV")
    type_pay = fields.Selection(pay_form, string="Type pay", default='paypar')
    total_sum = fields.Float(string="Total:", compute="_calc_total")
    in_tax_sum = fields.Float(string="Base:", compute="_calc_base")
    tax_sum = fields.Float(string="Tax:", compute="_calc_tax")
    state = fields.Selection(state_form, string="State", required=True, readonly=True, copy=False,
                             tracking=True, default='draft')
    invoices_count = fields.Integer(compute='compute_count')

    @api.model
    def create(self, vals):
        record = super(Codes_sells, self).create(vals)
        record.keycode_ids.code_id.write({'selled': True})
        record.keycode_ids.code_id.write({'sell_date': fields.Date.today()})
        return record

    def write(self, vals):
        for record in self:
            print(record.keycode_ids)
            record.keycode_ids.code_id.write({'selled': True})
        return super(Codes_sells, self).write(vals)

    def _calc_base(self):
        for record in self:
            key_register = record.keycode_ids
            total = 0
            for rec in key_register:
                total += rec.code_id.list_price
            record.in_tax_sum = total

    def _calc_total(self):
        for record in self:
            key_register = record.keycode_ids
            total = 0
            for rec in key_register:
                total += rec.code_id.standard_price
            record.total_sum = total

    def _calc_tax(self):
        for record in self:
            record.tax_sum = record.total_sum - record.in_tax_sum

    def invoiced(self):
        for rec in self:
            rec.write({
                'state': "invoiced"
            })
            invoice = rec.env['proyecto3.invoicesells'].create({
                'name': rec.name,
                'first_lastname': rec.first_lastname,
                'second_lastname': rec.second_lastname,
                'email': rec.email,
                'sell_date': rec.sell_date,
                'street': rec.street,
                'portal': rec.portal,
                'door': rec.door,
                'mobilphone': rec.mobilphone,
                'city': rec.city,
                'country_id': rec.country_id.id,
                'province_id': rec.province_id.id,
                'zip': rec.zip,
                'currency_id': rec.currency_id.id,
                'pay_count': rec.pay_count,
                'card_name': rec.card_name,
                'card_number': rec.card_number,
                'card_ex_month': rec.card_ex_month,
                'card_ex_year': rec.card_ex_year,
                'cvv': rec.cvv,
                'type_pay': rec.type_pay,
                'total_sum': rec.total_sum,
                'in_tax_sum': rec.in_tax_sum,
                'tax_sum': rec.tax_sum,
                'sell_id': rec.id,
            })
            for keys in rec.keycode_ids:
                rec.env['proyecto3.invoiceline'].create({
                    'code_id': keys.code_id.id,
                    'key_code': keys.key_code,
                    'creation_date': keys.creation_date,
                    'sell_date': keys.sell_date,
                    'selled': keys.selled,
                    'invoice_id': invoice.id,
                })

    def compute_count(self):
        for record in self:
            record.invoices_count = self.env['proyecto3.invoicesells'].search_count(
                [('sell_id', '=', self.id)])

    def get_invoices(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Invoices',
            'view_mode': 'tree,form',
            'res_model': 'proyecto3.invoicesells',
            'domain': [('sell_id', '=', self.id)],
            'context': "{'create': False}"
        }
