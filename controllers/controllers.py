# -*- coding: utf-8 -*-
# from odoo import http


# class StackMovePartnerId(http.Controller):
#     @http.route('/stack_move_partner_id/stack_move_partner_id/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/stack_move_partner_id/stack_move_partner_id/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('stack_move_partner_id.listing', {
#             'root': '/stack_move_partner_id/stack_move_partner_id',
#             'objects': http.request.env['stack_move_partner_id.stack_move_partner_id'].search([]),
#         })

#     @http.route('/stack_move_partner_id/stack_move_partner_id/objects/<model("stack_move_partner_id.stack_move_partner_id"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('stack_move_partner_id.object', {
#             'object': obj
#         })
