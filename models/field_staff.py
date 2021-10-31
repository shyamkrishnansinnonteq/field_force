from odoo import models, fields
class FieldStaffRecord(models.Model):
    _name = "field_force.field_staff"
    _description = 'Staff addition'
    
    name = fields.Char(string='Name', required=True)
    middle_name = fields.Char(string='Middle Name', required=True)
    last_name = fields.Char(string='Last Name', required=True)
    photo = fields.Binary(string='Photo')
    email = fields.Char(string='Email', required=True)
    phone = fields.Char(string='Phone Number', required=True)