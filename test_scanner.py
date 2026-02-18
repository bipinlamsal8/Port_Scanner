import unittest 
from port_scanner import validate_port
class TestScanner(unittest.TestCase): 
    def test_validate_port(self): 
        self.assertTrue(validate_port(80)) 