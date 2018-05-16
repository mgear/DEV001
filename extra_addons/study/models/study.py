# -*- coding: utf-8 -*-

from openerp import models, api, fields


class StudyFirstModule(models.Model):
    _name = 'study.study'

    name = fields.Char(string='Name')