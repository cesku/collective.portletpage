# -*- coding: utf-8 -*-
from Products.Five.browser import BrowserView
from plone.memoize.instance import memoize
from zope.component import getMultiAdapter


class Base(BrowserView):
    """Base class for index page views
    """
    @memoize
    def plone_view(self):
        return getMultiAdapter((self.context, self.request), name=u"plone_layout")


class TwoColumns(Base):
    """A two-column layout.
    """

    def _get_text(self):
        return getattr(self.context, 'text', None)

    def at_text(self):
        text = self._get_text()
        return text and hasattr(self.context, 'widget')

    def dx_text(self):
        text = self._get_text()
        return text and hasattr(text, 'output_relative_to')

    def hasColumnTop(self):
        ploneview = self.plone_view()
        return ploneview.have_portlets('collective.portletpage.toprow', view=self)

    def hasColumnFirst(self):
        ploneview = self.plone_view()
        return ploneview.have_portlets('collective.portletpage.firstcolumn', view=self)

    def hasColumnSecond(self):
        ploneview = self.plone_view()
        return ploneview.have_portlets('collective.portletpage.secondcolumn', view=self)

    def hasColumnBottom(self):
        ploneview = self.plone_view()
        return ploneview.have_portlets('collective.portletpage.bottomrow', view=self)
