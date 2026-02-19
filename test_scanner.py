import unittest 
from port_scanner import validate_port, validate_ip
class TestScanner(unittest.TestCase): 
    def test_validate_port(self):
        self.assertTrue(validate_port(80)) 
        self.assertTrue(validate_port(1)) 
        self.assertTrue(validate_port(65535))
        self.assertFalse(validate_port(0))
        self.assertFalse(validate_port(65536))

    def test_validate_ip(self):
        self.assertTrue(validate_ip("127.0.0.1"))
        self.assertFalse(validate_ip("256.256.256.256"))
        self.assertFalse(validate_ip("abc.def.ghi.jkl"))

if __name__ == '__main__':
    unittest.main()