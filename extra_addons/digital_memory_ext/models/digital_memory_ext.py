# -*- coding: utf-8 -*-


from openerp import models, fields, api


class CourseExt(models.Model):
#    _inherit = 'digital_memory.course'
    _name = 'digital_memory.course'
    _inherit = ['digital_memory.course', 'mail.thread']

    @api.multi
    @api.depends('attendees_ids')
    def _compute_attendees(self):
        for rec in self:
            rec.atnds_count = len(rec.attendees_ids)

#    description = fields.Html(string="Description")
    state = fields.Selection([ ('draft', 'Draft'),
                              ('confirm', 'Confirm'),
                              ('progres', 'In Progres'),
                              ('close', 'Closed') ], default='draft')
    active = fields.Boolean(string='Active', default=True)
    attendees_ids = fields.One2many('res.partner', 'course_id', string='attendees list')
    atnds_count = fields.Integer('Attendees', compute=_compute_attendees)


class Attendees(models.Model):

    _inherit = 'res.partner'
    course_id = fields.Many2one('digital_memory.course', string='Active course')
