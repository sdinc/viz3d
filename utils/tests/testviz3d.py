#!/usr/bin/env python

#--------------------------
#@author info@jbbs-inc.com  
#unit tests
#--------------------------

#python specific
import unittest
import os
import tempfile
import subprocess
import shlex
import pdb
import string
import sys

class testClassAttributes(unittest.TestCase):
    def setUp(self):
        pass

    def test_import(self):
        '''
        import the module
        '''
        try:
            import viz3d
        except:
            print "Error: not able to import viz3d make sure that the module in installed correctly"

    # def test_main(self):
    #     '''
    #     execute main
    #     '''
    #     import viz3d
    #     old_args = sys.argv
    #     sys.argv = ['viz3drun','--test-env']
    #     viz3d.main()
    #     sys.argv = old_args

    # def test_printhelp(self):
    #     '''
    #     print the help
    #     '''
    #     import viz3d
    #     old_args = sys.argv
    #     sys.argv = ['viz3drun']
    #     viz3d.main()
    #     sys.argv = old_args

    def tearDown(self):
        """
        cleanup 
        """
        pass
    
if __name__ == '__main__':
    unittest.main()
