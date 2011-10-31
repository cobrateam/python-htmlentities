# -*- encoding: utf-8 -*-

from unittest import TestCase

import htmlentities


class EncodingTestCase(TestCase):

    def test_should_encode_basic_entities(self):
        self.assertEqual('&amp;', htmlentities.encode('&'))
        self.assertEqual('&quot;', htmlentities.encode('"'))
        self.assertEqual('&lt;', htmlentities.encode('<'))

    def test_should_encode_utf8_accents(self):
        self.assertEqual('&eacute;', htmlentities.encode(u'é'))
        self.assertEqual('&ecirc;', htmlentities.encode(u'ê'))
