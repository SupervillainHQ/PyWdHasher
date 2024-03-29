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

import re
import sys
import getpass
import hashlib
import rules.Rules

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
    parser.add_argument("-r", "--rule", action='append', help="transform rule(s)")
    parser.add_argument("-a", "--algorithm", help="transform rule(s)", default="md5")
    
    # clipboard manager
    r = Tk()

    # Process arguments
    args = parser.parse_args()
    salt = getpass.getpass("salt: ")
    domain = r.clipboard_get()
    
    truncatLen = re.compile(r"^len:([\d]*)$")
    truncatNel = re.compile(r"^nel:([\d]*)$")
    specialLen = re.compile(r"^special:([\d]*)$")
    specialNel = re.compile(r"^laiceps:([\d]*)$")

    if args.algorithm == 'sha224':
        password = hashlib.sha224(domain + salt).hexdigest()
    elif args.algorithm == 'sha512':
        password = hashlib.sha512(domain + salt).hexdigest()
    else:
        password = hashlib.md5(domain + salt).hexdigest()
    
    for r in args.rule:
        if r == "uc":
            rule = rules.Rules.UC()
            password = rule.apply(password)
        elif r == "ucfirst":
            rule = rules.Rules.UCFirst()
            password = rule.apply(password)
        elif r == "uclast":
            rule = rules.Rules.UCLast()
            password = rule.apply(password)
        elif r == "reverse":
            rule = rules.Rules.Reverse()
            password = rule.apply(password)
        elif truncatLen.match(r):
            matches = truncatLen.search(r)
            l = matches.group(1)
            rule = rules.Rules.Truncate(int(l))
            password = rule.apply(password)
        elif truncatNel.match(r):
            matches = truncatNel.search(r)
            l = matches.group(1)
            rule = rules.Rules.Truncate(int(l), reverse=True)
            password = rule.apply(password)
        elif specialLen.match(r):
            matches = specialLen.search(r)
            l = matches.group(1)
            rule = rules.Rules.Special(int(l))
            password = rule.apply(password)
        elif specialNel.match(r):
            matches = specialNel.search(r)
            l = matches.group(1)
            rule = rules.Rules.Special(int(l), reverse=True)
            password = rule.apply(password)

    if args.out is True:
        print "password for domain '" + domain + "':"
        print password
    else:
        r.clipboard_append(password)
        print "password for domain '" + domain + "' is added to clipboard..."
        r.update()
        r.destroy()
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