import unittest
import doctest
from plone.testing import layered

from collective.portletpage.tests import base

optionflags = doctest.REPORT_ONLY_FIRST_FAILURE | doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS


def test_suite():
    return unittest.TestSuite([

        # Demonstrate the main content types
        layered(doctest.DocFileSuite(
            'tests/content.txt', package='collective.portletpage',
            optionflags=optionflags),
            layer=base.COLLECTIVE_PORTLETPAGE_FUNCTIONAL_TESTING),

        # Demonstrate the portlet assignment
        layered(doctest.DocFileSuite(
            'tests/portletassignment.txt', package='collective.portletpage',
            optionflags=optionflags),
            layer=base.COLLECTIVE_PORTLETPAGE_FUNCTIONAL_TESTING),

        # Demonstrate the main content types (Dexterity version)
        layered(doctest.DocFileSuite(
            'tests/dx_content.txt', package='collective.portletpage',
            optionflags=optionflags),
            layer=base.DX_COLLECTIVE_PORTLETPAGE_FUNCTIONAL_TESTING),

        # Demonstrate the portlet assignment (Dexterity version)
        layered(doctest.DocFileSuite(
            'tests/dx_portletassignment.txt', package='collective.portletpage',
            optionflags=optionflags),
            layer=base.DX_COLLECTIVE_PORTLETPAGE_FUNCTIONAL_TESTING),

        ]


    )
