from odoo import http
from odoo.http import request


class Game(http.Controller):

    @http.route('/cantidad', type="http", auth="public", website=True)
    def incidence(self, **kw):
        return http.request.render('proyecto3.create_cantidad', {})
