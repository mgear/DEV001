# -*- coding: utf-8 -*-

from openerp import models, api, fields


class StudyModuleExtention(models.Model):
    _inherit = 'study.study'
    # _name = 'study.study'
    # _inherit = ['study.study', 'mail.thread']

    @api.multi
    @api.depends('students_ids')
    def _compute_students(self):
        for rec in self:
            rec.stud_count = len(rec.students_ids)

    name = fields.Char(string='Course name')
    description = fields.Html(string='Course description')
    active = fields.Boolean(string='Active', default=True)
    # state = fields.Selection([('stay', 'Waiting for students'),
    #                           ('go', 'In progress'),
    #                           ('closed', 'Finished')], default='stay')
    # students_ids = fields.One2many('res.partner', 'course_id', string='students list')
    # stud_count = fields.Integer('Students', compute=_compute_students)


# class StudentsModuleExtention(models.Model):
#     _inherit = 'res.partner'
#
#     course_id = fields.Many2one('study.study', string='Active course')

