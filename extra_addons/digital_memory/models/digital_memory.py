# -*- coding: utf-8 -*-


from openerp import models, fields, api

class Course(models.Model):
    _name = 'digital_memory.course'

    name = fields.Char(string="Title", required=True)
    description = fields.Text()
    is_done = fields.Boolean(string='Done')