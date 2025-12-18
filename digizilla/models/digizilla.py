from odoo import models, fields, api

class Digizilla(models.Model):
    _name = 'digizilla.record'
    _description = 'Digizilla Record'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', required=True, tracking=True)
    gender = fields.Selection([('male','Male'),('female','Female')], string='Gender', tracking=True)
    country = fields.Char(string='Country', tracking=True)
    joining_date = fields.Date(string='Joining Date', tracking=True)
    tags = fields.Char(string='Tags', tracking=True)
    customers_ids = fields.Many2many('res.partner', string='Customers', tracking=True)
    company_id = fields.Many2one('res.company', string='Company', required=True, tracking=True)
    notes = fields.Text(string='Notes', tracking=True)
    comments = fields.Char(string='Comments', tracking=True)
