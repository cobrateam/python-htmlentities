# -*- encoding: utf-8 -*-

from unittest import TestCase

import htmlentities


class DecodingTestCase(TestCase):

    def test_should_decode_basic_entities(self):
        self.assertEqual('&', htmlentities.decode('&amp;'))
        self.assertEqual('"', htmlentities.decode('&quot;'))
        self.assertEqual('<', htmlentities.decode('&lt;'))

    def test_should_decode_utf8_accents(self):
        self.assertEqual(u'é', htmlentities.decode('&eacute;'))
        self.assertEqual(u'ê', htmlentities.decode('&ecirc;'))
