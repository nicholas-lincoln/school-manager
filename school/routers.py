# -*- coding: utf-8 -*-
class SchoolRouter:
    """
    A router to control all database operations on models in the school app.
    """

    def db_for_read(self, model, **hints):
        """
        Attempts to read school models go to the 'school' database.
        """
        if model._meta.app_label == 'school':
            return 'school'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write school models go to the 'school' database.
        """
        if model._meta.app_label == 'school':
            return 'school'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the school app is involved.
        """
        if obj1._meta.app_label == 'school' or \
                obj2._meta.app_label == 'school':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Ensure that the school app's models get created on the 'school' database.
        """
        if app_label == 'school':
            return db == 'school'
        return None
