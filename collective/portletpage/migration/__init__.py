# -*- coding: utf-8 -*-
from Products.Five.browser import BrowserView
from plone.app.contenttypes.migration.migration import migrateCustomAT
from plone.protect.interfaces import IDisableCSRFProtection
from zope.interface import alsoProvides


class MigrateAtPortletPage(BrowserView):

    def __call__(self):
        if 'migrate' in self.request.form:
            alsoProvides(self.request, IDisableCSRFProtection)
            return self._migration()
        else:
            return self._message()

    def _migration(self):
        fields_mapping = ({
            'AT_field_name': 'text',
            'DX_field_name': 'text',
            'DX_field_type': 'RichText',
        })

        migrateCustomAT(
            fields_mapping,
            src_type='Portlet Page',
            dst_type='DXPortlet_Page')

        return 'Done!'

    def _message(self):
        portal = self.context
        msg = """
        Open this url to run the migration:
            %(portal_url)s?migrate=1

        There are %(number)s Portlet Page to be migrated
        """ % {
            "portal_url": portal.absolute_url(),
            "number": len(portal.portal_catalog(portal_type='Portlet Page'))
        }
        return msg
