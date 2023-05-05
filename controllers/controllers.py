# -*- coding: utf-8 -*-
# from odoo import http


# class Proyecto3(http.Controller):
#     @http.route('/proyecto3/proyecto3', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/proyecto3/proyecto3/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('proyecto3.listing', {
#             'root': '/proyecto3/proyecto3',
#             'objects': http.request.env['proyecto3.proyecto3'].search([]),
#         })

#     @http.route('/proyecto3/proyecto3/objects/<model("proyecto3.proyecto3"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('proyecto3.object', {
#             'object': obj
#         })
