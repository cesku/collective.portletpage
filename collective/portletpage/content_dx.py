from plone.app.contenttypes.content import Document
from plone.app.contenttypes.interfaces import IDocument
from zope.interface import implementer


@implementer(IDocument)
class PortletPage(Document):
    """Convenience subclass for ``PortletPage`` portal type
    """
