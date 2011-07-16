from unittest import TestCase

import htmlentities


class EncodingTestCase(TestCase):

    def test_should_encode_basic_entities(self):
        self.assertEqual('&amp;', htmlentities.encode('&'))
        self.assertEqual('&quot;', htmlentities.encode('"'))
        self.assertEqual('&lt;', htmlentities.encode('<'))
