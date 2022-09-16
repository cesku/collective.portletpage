#!/bin/sh

DOMAIN='collective.portletpage'
I18NDUDE=../../bin/i18ndude

$I18NDUDE rebuild-pot --pot locales/${DOMAIN}.pot --create ${DOMAIN} .
$I18NDUDE merge --pot locales/${DOMAIN}.pot --merge locales/${DOMAIN}-manual.pot
$I18NDUDE sync --pot locales/${DOMAIN}.pot locales/*/LC_MESSAGES/${DOMAIN}.po
