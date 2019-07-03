#!/usr/local/bin/python2.7
# encoding: utf-8
'''
svhq.pywdhasher.PasswordHasher -- shortdesc

svhq.pywdhasher.PasswordHasher is a description

It defines classes_and_methods

@author:     user_name

@copyright:  2019 organization_name. All rights reserved.

@license:    license

@contact:    user_email
@deffield    updated: Updated
'''

import sys
import getpass
import hashlib
import time

from argparse import ArgumentParser
from Tkinter import Tk

__all__ = []
__version__ = 0.1
__date__ = '2019-07-03'
__updated__ = '2019-07-03'

DEBUG = 1
TESTRUN = 0
PROFILE = 0

class CLIError(Exception):
    '''Generic exception to raise and log different fatal errors.'''
    def __init__(self, msg):
        super(CLIError).__init__(type(self))
        self.msg = "E: %s" % msg
    def __str__(self):
        return self.msg
    def __unicode__(self):
        return self.msg

def main(argv=None): # IGNORE:C0111
    '''Command line options.'''

    if argv is None:
        argv = sys.argv
    else:
        sys.argv.extend(argv)

    # Setup argument parser
    parser = ArgumentParser()
    parser.add_argument("-o", "--out", action="store_true", help="output password in tty instead of inserting in clipboard")
    parser.add_argument("-r", "--rule", help="transform rule(s)")
    
    # clipboard manager
    r = Tk()

    # Process arguments
    args = parser.parse_args()
    salt = getpass.getpass("salt: ")
    domain = r.clipboard_get()

    password = hashlib.md5(domain + salt).hexdigest()

    if args.out is True:
        print "password for domain '" + domain + "':"
        print password
    else:
        r.clipboard_append(password)
        print "password for domain '" + domain + "' is added to clipboard..."
        r.update()
        r.destroy()
#        time.sleep(1)
        raw_input("Paste password into password-field, then hit Enter to exit")

    return 0

if __name__ == "__main__":
#     if DEBUG:
#         sys.argv.append("-h")
#         sys.argv.append("-v")
#         sys.argv.append("-r")
#     if TESTRUN:
#         import doctest
#         doctest.testmod()
#     if PROFILE:
#         import cProfile
#         import pstats
#         profile_filename = 'svhq.pywdhasher.PasswordHasher_profile.txt'
#         cProfile.run('main()', profile_filename)
#         statsfile = open("profile_stats.txt", "wb")
#         p = pstats.Stats(profile_filename, stream=statsfile)
#         stats = p.strip_dirs().sort_stats('cumulative')
#         stats.print_stats()
#         statsfile.close()
#         sys.exit(0)
    sys.exit(main())