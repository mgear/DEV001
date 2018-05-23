# -*- coding: utf-8 -*-
# Файл python должен начинаться с этой строки

from openerp import models, api, fields


class StudyFirstModule(models.Model):
    # Основной суперкласс для регулярных моделей OpenERP, поддерживающих базу данных.
    # Модели OpenERP создаются путем наследования от этого класса
    _name = 'study.study'
    # _name наименование бизнес - объекта, в dot - нотации(в пространстве имен модуля)

    name = fields.Char(string='Name')
    # По умолчанию Odoo так же требует поле name для всех моделей данных для различных типов отображения и
    # поиска.Поле, используемое для этих целей может быть отменено _rec_name

    start_date = fields.Date(string='Start date')
    end_date = fields.Date(string='End date')
    is_done = fields.Boolean(string='Done')
    # Подобно самой модели данных, ее поля могут быть настроены путем передачи значений атрибутов в качестве параметров
