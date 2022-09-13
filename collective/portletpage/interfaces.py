# -*- coding: utf-8 -*-
from collective.portletpage import MessageFactory as _
from plone.app.portlets.interfaces import IColumn
from plone.portlets.interfaces import IPortletManager
from zope import schema
from zope.interface import Interface
from plone.app.contenttypes.interfaces import IDocument


class IPortletPage(IDocument):
    """Content type interface for portlet pages
    """


class IPortletPageColumn(IPortletManager, IColumn):
    """Marker interface describing columns on a portlet page
    """
