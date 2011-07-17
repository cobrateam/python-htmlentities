from unittest import TestCase

import htmlentities


class DecodingTestCase(TestCase):

    def test_should_decode_basic_entities(self):
        self.assertEqual('&', htmlentities.decode('&amp;'))
        self.assertEqual('"', htmlentities.decode('&quot;'))
        self.assertEqual('<', htmlentities.decode('&lt;'))
