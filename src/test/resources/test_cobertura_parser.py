#!/usr/bin/python
 
import unittest

import os
parentdir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.sys.path.insert(0,parentdir + "/main/resources/cobertura") 

import cobertura_parser
 
class CoberturaParserTest(unittest.TestCase):
    """Sample test case"""
     
    # preparing to test
    def setUp(self):
        """ Setting up for the test """
        print "CoberturaParserTest:setUp_:begin"
        ## do something...
        print "CoberturaParserTest:setUp_:end"
     
    # ending the test
    def tearDown(self):
        """Cleaning up after the test"""
        print "CoberturaParserTest:tearDown_:begin"
        ## do something...
        print "CoberturaParserTest:tearDown_:end"
     
    # test routine A
    def testA(self):
        """Test routine A"""
        cobertura_parser.main([os.path.abspath(__file__) + "/cobertura.xml"], {})
     
    # test routine B
    def testB(self):
        """Test routine B"""
        print "CoberturaParserTest:testB"

unittest.main()