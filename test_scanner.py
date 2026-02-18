import unittest 
from port_scanner import validate_port
class TestScanner(unittest.TestCase): 
    def test_validate_port(self):
        self.assertTrue(validate_port(80)) 
        self.assertTrue(validate_port(1)) 
        self.assertTrue(validate_port(65535))
        self.assertFalse(validate_port(0))
        self.assertFalse(validate_port(65536))