# -*- coding: utf-8 -*-
# from odoo import http


# class L10nBoBicurrency(http.Controller):
#     @http.route('/l10n_bo_bicurrency/l10n_bo_bicurrency/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/l10n_bo_bicurrency/l10n_bo_bicurrency/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('l10n_bo_bicurrency.listing', {
#             'root': '/l10n_bo_bicurrency/l10n_bo_bicurrency',
#             'objects': http.request.env['l10n_bo_bicurrency.l10n_bo_bicurrency'].search([]),
#         })

#     @http.route('/l10n_bo_bicurrency/l10n_bo_bicurrency/objects/<model("l10n_bo_bicurrency.l10n_bo_bicurrency"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('l10n_bo_bicurrency.object', {
#             'object': obj
#         })
