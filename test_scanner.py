import unittest
from port_scanner import validate_port, validate_ip, scan_single_port, PortResult
import time

class TestScanner(unittest.TestCase):
    # IP valid testing
    def test_validate_ip_valid(self):
        self.assertTrue(validate_ip("192.168.1.1"))
        self.assertTrue(validate_ip("127.0.0.1"))
        self.assertTrue(validate_ip("0.0.0.0"))

    def test_validate_ip_invalid_range(self):
        self.assertFalse(validate_ip("256.256.256.256"))
        self.assertFalse(validate_ip("192.168.1.999"))

    def test_validate_ip_invalid_format(self):
        self.assertFalse(validate_ip("abc.def.ghi.jkl"))
        self.assertFalse(validate_ip("192.168.1")) # Missing 4th octet
        self.assertFalse(validate_ip("192.168.1.1.1")) # Too many octets

    # Port valid testing
    def test_validate_port(self):
        self.assertTrue(validate_port(80))
        self.assertTrue(validate_port(1))
        self.assertTrue(validate_port(65535))
        self.assertFalse(validate_port(0))
        self.assertFalse(validate_port(65536))

    # Single port scanning test
    def test_scan_single_port(self):
        status, service = scan_single_port("127.0.0.1", 54321)
        self.assertNotEqual(status, "OPEN") 

    # PortResult display test
    def test_port_result_display(self):
        timestamp = time.time()
        result = PortResult(80, "OPEN", "http", timestamp)
        display_str = result.display()
        
        # Checks that the display string contains the expected information
        self.assertIn("80", display_str)
        self.assertIn("http", display_str)
        self.assertIn("OPEN", display_str)

def load_suite():
    suite = unittest.TestSuite()
    
    #adding tests to the suite
    suite.addTest(TestScanner('test_validate_port'))
    suite.addTest(TestScanner('test_validate_ip_valid'))
    suite.addTest(TestScanner('test_validate_ip_invalid_range'))
    suite.addTest(TestScanner('test_validate_ip_invalid_format'))
    suite.addTest(TestScanner('test_scan_single_port'))
    suite.addTest(TestScanner('test_port_result_display'))
    
    return suite

if __name__ == "__main__":
    print("Running Custom Suite...")
    
    #creating the test suite 
    my_suite = load_suite()
    
    #running the test suite
    runner = unittest.TextTestRunner(verbosity=2) 
    #verbosity=2 gives detailed output
    
    result = runner.run(my_suite)