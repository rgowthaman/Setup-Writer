import os
import sys
import argparse
from colorama import *

init(convert=True)


def get_argument():
    parser = argparse.ArgumentParser(usage="pip-setup [options]", epilog='Press ENTER For default input')
    parser.add_argument('-v', '--version', action='version', help='show version number and exit', version="1.2.1")
    group = parser.add_argument_group("to show help")
    group.add_argument("--print-default", default=False, action='store_true', help='show default values and exit')
    group.add_argument("--classifier", default=False, metavar='', help='show the available in classifier category')
    group.add_argument("--avail-classifier", default=False, action='store_const', const='all',
                       help='show all the available classifiers')
    group.add_argument("--classifier-category", default=False, action='store_true', help=argparse.SUPPRESS)
    parser.add_argument_group(group)
    options = parser.parse_args()
    return options


def get_upload_argument():
    parser = argparse.ArgumentParser(usage="pip-upload [options]", )
    parser.add_argument('-v', '--version', action='version', help='show version number and exit', version="1.2.1")
    group = parser.add_argument_group("to help in uploading your package")
    group.add_argument("-u", "--upload-to", default='test pip', metavar='',
                       help='either real pip or test pip (default: %(default)s)')
    group.add_argument("-p", "--path", default=os.getcwd(), metavar='', help='path to the package (default: %(default)s))')
    parser.add_argument_group(group)
    options = parser.parse_args()
    return options


class Classifiers:
    def __init__(self):
        self.classifiers_available = ['Development Status :: 1 - Planning',
                                      'Development Status :: 2 - Pre-Alpha',
                                      'Development Status :: 3 - Alpha',
                                      'Development Status :: 4 - Beta',
                                      'Development Status :: 5 - Production/Stable',
                                      'Development Status :: 6 - Mature',
                                      'Development Status :: 7 - Inactive',
                                      'Environment :: Console',
                                      'Environment :: Console :: Curses',
                                      'Environment :: Console :: Framebuffer',
                                      'Environment :: Console :: Newt',
                                      'Environment :: Console :: svgalib',
                                      'Environment :: GPU',
                                      'Environment :: GPU :: NVIDIA CUDA',
                                      'Environment :: GPU :: NVIDIA CUDA :: 1.0',
                                      'Environment :: GPU :: NVIDIA CUDA :: 1.1',
                                      'Environment :: GPU :: NVIDIA CUDA :: 2.0',
                                      'Environment :: GPU :: NVIDIA CUDA :: 2.1',
                                      'Environment :: GPU :: NVIDIA CUDA :: 2.2',
                                      'Environment :: GPU :: NVIDIA CUDA :: 2.3',
                                      'Environment :: GPU :: NVIDIA CUDA :: 3.0',
                                      'Environment :: GPU :: NVIDIA CUDA :: 3.1',
                                      'Environment :: GPU :: NVIDIA CUDA :: 3.2',
                                      'Environment :: GPU :: NVIDIA CUDA :: 4.0',
                                      'Environment :: GPU :: NVIDIA CUDA :: 4.1',
                                      'Environment :: GPU :: NVIDIA CUDA :: 4.2',
                                      'Environment :: GPU :: NVIDIA CUDA :: 5.0',
                                      'Environment :: GPU :: NVIDIA CUDA :: 5.5',
                                      'Environment :: GPU :: NVIDIA CUDA :: 6.0',
                                      'Environment :: GPU :: NVIDIA CUDA :: 6.5',
                                      'Environment :: GPU :: NVIDIA CUDA :: 7.0',
                                      'Environment :: GPU :: NVIDIA CUDA :: 7.5',
                                      'Environment :: GPU :: NVIDIA CUDA :: 8.0',
                                      'Environment :: GPU :: NVIDIA CUDA :: 9.0',
                                      'Environment :: GPU :: NVIDIA CUDA :: 9.1',
                                      'Environment :: GPU :: NVIDIA CUDA :: 9.2',
                                      'Environment :: GPU :: NVIDIA CUDA :: 10.0',
                                      'Environment :: GPU :: NVIDIA CUDA :: 10.1',
                                      'Environment :: GPU :: NVIDIA CUDA :: 10.2',
                                      'Environment :: GPU :: NVIDIA CUDA :: 11.0',
                                      'Environment :: GPU :: NVIDIA CUDA :: 11.1',
                                      'Environment :: GPU :: NVIDIA CUDA :: 11.2',
                                      "Environment :: Handhelds/PDA's",
                                      'Environment :: MacOS X',
                                      'Environment :: MacOS X :: Aqua',
                                      'Environment :: MacOS X :: Carbon',
                                      'Environment :: MacOS X :: Cocoa',
                                      'Environment :: No Input/Output (Daemon)',
                                      'Environment :: OpenStack',
                                      'Environment :: Other Environment',
                                      'Environment :: Plugins',
                                      'Environment :: Web Environment',
                                      'Environment :: W',
                                      'Environment :: Buffet',
                                      'Environment :: W',
                                      'Environment :: Mozilla',
                                      'Environment :: W',
                                      'Environment :: ToscaWidgets',
                                      'Environment :: Win32 (MS Windows)',
                                      'Environment :: X11 Applications',
                                      'Environment :: X11 Applications :: GTK',
                                      'Environment :: X11 Applications :: Gnome',
                                      'Environment :: X11 Applications :: KDE',
                                      'Environment :: X11 Applications :: Qt',
                                      'Framework :: AWS CDK',
                                      'Framework :: AWS CDK :: 1',
                                      'Framework :: AiiDA',
                                      'Framework :: Ansible',
                                      'Framework :: AsyncIO',
                                      'Framework :: BEAT',
                                      'Framework :: BFG',
                                      'Framework :: Bob',
                                      'Framework :: Bottle',
                                      'Framework :: Buildout',
                                      'Framework :: Buildout :: Extension',
                                      'Framework :: Buildout :: Recipe',
                                      'Framework :: CastleCMS',
                                      'Framework :: CastleCMS :: Theme',
                                      'Framework :: Chandler',
                                      'Framework :: CherryPy',
                                      'Framework :: CubicWeb',
                                      'Framework :: Dash',
                                      'Framework :: Django',
                                      'Framework :: Django :: 1.4',
                                      'Framework :: Django :: 1.5',
                                      'Framework :: Django :: 1.6',
                                      'Framework :: Django :: 1.7',
                                      'Framework :: Django :: 1.8',
                                      'Framework :: Django :: 1.9',
                                      'Framework :: Django :: 1.10',
                                      'Framework :: Django :: 1.11',
                                      'Framework :: Django :: 2.0',
                                      'Framework :: Django :: 2.1',
                                      'Framework :: Django :: 2.2',
                                      'Framework :: Django :: 3.0',
                                      'Framework :: Django :: 3.1',
                                      'Framework :: Django :: 3.2',
                                      'Framework :: Django CMS',
                                      'Framework :: Django CMS :: 3.4',
                                      'Framework :: Django CMS :: 3.5',
                                      'Framework :: Django CMS :: 3.6',
                                      'Framework :: Django CMS :: 3.7',
                                      'Framework :: Django CMS :: 3.8',
                                      'Framework :: Flake8',
                                      'Framework :: Flask',
                                      'Framework :: Hypothesis',
                                      'Framework :: IDLE',
                                      'Framework :: IPython',
                                      'Framework :: Jupyter',
                                      'Framework :: Jupyter :: JupyterLab',
                                      'Framework :: Jupyter :: JupyterLab :: 1',
                                      'Framework :: Jupyter :: JupyterLab :: 2',
                                      'Framework :: Jupyter :: JupyterLab :: 3',
                                      'Framework :: Jupyter :: JupyterLab :: 4',
                                      'Framework :: Jupyter :: JupyterLab :: Extensions',
                                      'Framework :: Jupyter :: JupyterLab :: Extensions :: Mime Renderers',
                                      'Framework :: Jupyter :: JupyterLab :: Extensions :: Prebuilt',
                                      'Framework :: Jupyter :: JupyterLab :: Extensions :: Themes',
                                      'Framework :: Kedro',
                                      'Framework :: Lektor',
                                      'Framework :: Masonite',
                                      'Framework :: Matplotlib',
                                      'Framework :: Nengo',
                                      'Framework :: Odoo',
                                      'Framework :: Opps',
                                      'Framework :: Paste',
                                      'Framework :: Pelican',
                                      'Framework :: Pelican :: Plugins',
                                      'Framework :: Pelican :: Themes',
                                      'Framework :: Plone',
                                      'Framework :: Plone :: 3.2',
                                      'Framework :: Plone :: 3.3',
                                      'Framework :: Plone :: 4.0',
                                      'Framework :: Plone :: 4.1',
                                      'Framework :: Plone :: 4.2',
                                      'Framework :: Plone :: 4.3',
                                      'Framework :: Plone :: 5.0',
                                      'Framework :: Plone :: 5.1',
                                      'Framework :: Plone :: 5.2',
                                      'Framework :: Plone :: 5.3',
                                      'Framework :: Plone :: 6.0',
                                      'Framework :: Plone :: Addon',
                                      'Framework :: Plone :: Core',
                                      'Framework :: Plone :: Theme',
                                      'Framework :: Pylons',
                                      'Framework :: Pyramid',
                                      'Framework :: Pytest',
                                      'Framework :: Review Board',
                                      'Framework :: Robot Framework',
                                      'Framework :: Rob',
                                      'Framework :: Library',
                                      'Framework :: Rob',
                                      'Framework :: Tool',
                                      'Framework :: Scrapy',
                                      'Framework :: Setuptools Plugin',
                                      'Framework :: Sphinx',
                                      'Framework :: Sphinx :: Extension',
                                      'Framework :: Sphinx :: Theme',
                                      'Framework :: Trac',
                                      'Framework :: Trio',
                                      'Framework :: Tryton',
                                      'Framework :: TurboGears',
                                      'Framework :: TurboGears :: Applications',
                                      'Framework :: TurboGears :: Widgets',
                                      'Framework :: Twisted',
                                      'Framework :: Wagtail',
                                      'Framework :: Wagtail :: 1',
                                      'Framework :: Wagtail :: 2',
                                      'Framework :: ZODB',
                                      'Framework :: Zope',
                                      'Framework :: Zope2',
                                      'Framework :: Zope3',
                                      'Framework :: Zope :: 2',
                                      'Framework :: Zope :: 3',
                                      'Framework :: Zope :: 4',
                                      'Framework :: Zope :: 5',
                                      'Framework :: aiohttp',
                                      'Framework :: cocotb',
                                      'Framework :: napari',
                                      'Framework :: tox',
                                      'Intended Audience :: Customer Service',
                                      'Intended Audience :: Developers',
                                      'Intended Audience :: Education',
                                      'Intended Audience :: End Users/Desktop',
                                      'Intended Audience :: Financial and Insurance Industry',
                                      'Intended Audience :: Healthcare Industry',
                                      'Intended Audience :: Information Technology',
                                      'Intended Audience :: Legal Industry',
                                      'Intended Audience :: Manufacturing',
                                      'Intended Audience :: Other Audience',
                                      'Intended Audience :: Religion',
                                      'Intended Audience :: Science/Research',
                                      'Intended Audience :: System Administrators',
                                      'Intended Audience :: Telecommunications Industry',
                                      'License :: Aladdin Free Public License (AFPL)',
                                      'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
                                      'License :: CeCILL-B Free Software License Agreement (CECILL-B)',
                                      'License :: CeCILL-C Free Software License Agreement (CECILL-C)',
                                      'License :: DFSG approved',
                                      'License :: Eiffel Forum License (EFL)',
                                      'License :: Free For Educational Use',
                                      'License :: Free For Home Use',
                                      'License :: Free To Use But Restricted',
                                      'License :: Free for non-commercial use',
                                      'License :: Freely Distributable',
                                      'License :: Freeware',
                                      'License :: GUST Font License 1.0',
                                      'License :: GUST Font License 2006-09-30',
                                      'License :: Netscape Public License (NPL)',
                                      'License :: Nokia Open Source License (NOKOS)',
                                      'License :: OSI Approved',
                                      'License :: OSI Approved :: Academic Free License (AFL)',
                                      'License :: OSI Approved :: Apache Software License',
                                      'License :: OSI Approved :: Apple Public Source License',
                                      'License :: OSI Approved :: Artistic License',
                                      'License :: OSI Approved :: Attribution Assurance License',
                                      'License :: OSI Approved :: BSD License',
                                      'License :: OSI Approved :: Boost Software License 1.0 (BSL-1.0)',
                                      'License :: OSI Approved :: CEA CNRS Inria Logiciel Libre License, version 2.1 (CeCILL-2.1)',
                                      'License :: OSI Approved :: Common Development and Distribution License 1.0 (CDDL-1.0)',
                                      'License :: OSI Approved :: Common Public License',
                                      'License :: OSI Approved :: Eclipse Public License 1.0 (EPL-1.0)',
                                      'License :: OSI Approved :: Eclipse Public License 2.0 (EPL-2.0)',
                                      'License :: OSI Approved :: Eiffel Forum License',
                                      'License :: OSI Approved :: European Union Public Licence 1.0 (EUPL 1.0)',
                                      'License :: OSI Approved :: European Union Public Licence 1.1 (EUPL 1.1)',
                                      'License :: OSI Approved :: European Union Public Licence 1.2 (EUPL 1.2)',
                                      'License :: OSI Approved :: GNU Affero General Public License v3',
                                      'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
                                      'License :: OSI Approved :: GNU Free Documentation License (FDL)',
                                      'License :: OSI Approved :: GNU General Public License (GPL)',
                                      'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
                                      'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
                                      'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
                                      'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
                                      'License :: OSI Approved :: GNU Lesser General Public License v2 (LGPLv2)',
                                      'License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)',
                                      'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
                                      'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
                                      'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
                                      'License :: OSI Approved :: Historical Permission Notice and Disclaimer (HPND)',
                                      'License :: OSI Approved :: IBM Public License',
                                      'License :: OSI Approved :: ISC License (ISCL)',
                                      'License :: OSI Approved :: Intel Open Source License',
                                      'License :: OSI Approved :: Jabber Open Source License',
                                      'License :: OSI Approved :: MIT License',
                                      'License :: OSI Approved :: MIT No Attribution License (MIT-0)',
                                      'License :: OSI Approved :: MITRE Collaborative Virtual Workspace License (CVW)',
                                      'License :: OSI Approved :: MirOS License (MirOS)',
                                      'License :: OSI Approved :: Motosoto License',
                                      'License :: OSI Approved :: Mozilla Public License 1.0 (MPL)',
                                      'License :: OSI Approved :: Mozilla Public License 1.1 (MPL 1.1)',
                                      'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
                                      'License :: OSI Approved :: Nethack General Public License',
                                      'License :: OSI Approved :: Nokia Open Source License',
                                      'License :: OSI Approved :: Open Group Test Suite License',
                                      'License :: OSI Approved :: Open Software License 3.0 (OSL-3.0)',
                                      'License :: OSI Approved :: PostgreSQL License',
                                      'License :: OSI Approved :: Python License (CNRI Python License)',
                                      'License :: OSI Approved :: Python Software Foundation License',
                                      'License :: OSI Approved :: Qt Public License (QPL)',
                                      'License :: OSI Approved :: Ricoh Source Code Public License',
                                      'License :: OSI Approved :: SIL Open Font License 1.1 (OFL-1.1)',
                                      'License :: OSI Approved :: Sleepycat License',
                                      'License :: OSI Approved :: Sun Industry Standards Source License (SISSL)',
                                      'License :: OSI Approved :: Sun Public License',
                                      'License :: OSI Approved :: The Unlicense (Unlicense)',
                                      'License :: OSI Approved :: Universal Permissive License (UPL)',
                                      'License :: OSI Approved :: University of Illinois/NCSA Open Source License',
                                      'License :: OSI Approved :: Vovida Software License 1.0',
                                      'License :: OSI Approved :: W3C License',
                                      'License :: OSI Approved :: X.Net License',
                                      'License :: OSI Approved :: Zope Public License',
                                      'License :: OSI Approved :: zlib/libpng License',
                                      'License :: Other/Proprietary License',
                                      'License :: Public Domain',
                                      'License :: Repoze Public License',
                                      'Natural Language :: Afrikaans',
                                      'Natural Language :: Arabic',
                                      'Natural Language :: Basque',
                                      'Natural Language :: Bengali',
                                      'Natural Language :: Bosnian',
                                      'Natural Language :: Bulgarian',
                                      'Natural Language :: Cantonese',
                                      'Natural Language :: Catalan',
                                      'Natural Language :: Chinese (Simplified)',
                                      'Natural Language :: Chinese (Traditional)',
                                      'Natural Language :: Croatian',
                                      'Natural Language :: Czech',
                                      'Natural Language :: Danish',
                                      'Natural Language :: Dutch',
                                      'Natural Language :: English',
                                      'Natural Language :: Esperanto',
                                      'Natural Language :: Finnish',
                                      'Natural Language :: French',
                                      'Natural Language :: Galician',
                                      'Natural Language :: German',
                                      'Natural Language :: Greek',
                                      'Natural Language :: Hebrew',
                                      'Natural Language :: Hindi',
                                      'Natural Language :: Hungarian',
                                      'Natural Language :: Icelandic',
                                      'Natural Language :: Indonesian',
                                      'Natural Language :: Irish',
                                      'Natural Language :: Italian',
                                      'Natural Language :: Japanese',
                                      'Natural Language :: Javanese',
                                      'Natural Language :: Korean',
                                      'Natural Language :: Latin',
                                      'Natural Language :: Latvian',
                                      'Natural Language :: Lithuanian',
                                      'Natural Language :: Macedonian',
                                      'Natural Language :: Malay',
                                      'Natural Language :: Marathi',
                                      'Natural Language :: Nepali',
                                      'Natural Language :: Norwegian',
                                      'Natural Language :: Panjabi',
                                      'Natural Language :: Persian',
                                      'Natural Language :: Polish',
                                      'Natural Language :: Portuguese',
                                      'Natural Language :: Portuguese (Brazilian)',
                                      'Natural Language :: Romanian',
                                      'Natural Language :: Russian',
                                      'Natural Language :: Serbian',
                                      'Natural Language :: Slovak',
                                      'Natural Language :: Slovenian',
                                      'Natural Language :: Spanish',
                                      'Natural Language :: Swedish',
                                      'Natural Language :: Tamil',
                                      'Natural Language :: Telugu',
                                      'Natural Language :: Thai',
                                      'Natural Language :: Tibetan',
                                      'Natural Language :: Turkish',
                                      'Natural Language :: Ukrainian',
                                      'Natural Language :: Urdu',
                                      'Natural Language :: Vietnamese',
                                      'Operating System :: Android',
                                      'Operating System :: BeOS',
                                      'Operating System :: MacOS',
                                      'Operating System :: MacOS :: MacOS 9',
                                      'Operating System :: MacOS :: MacOS X',
                                      'Operating System :: Microsoft',
                                      'Operating System :: Microsoft :: MS-DOS',
                                      'Operating System :: Microsoft :: Windows',
                                      'Operating System :: Microsoft :: Windows :: Windows 3.1 or Earlier',
                                      'Operating System :: Microsoft :: Windows :: Windows 7',
                                      'Operating System :: Microsoft :: Windows :: Windows 8',
                                      'Operating System :: Microsoft :: Windows :: Windows 8.1',
                                      'Operating System :: Microsoft :: Windows :: Windows 10',
                                      'Operating System :: Microsoft :: Windows :: Windows 95/98/2000',
                                      'Operating System :: Microsoft :: Windows :: Windows CE',
                                      'Operating System :: Microsoft :: Windows :: Windows NT/2000',
                                      'Operating System :: Microsoft :: Windows :: Windows Server 2003',
                                      'Operating System :: Microsoft :: Windows :: Windows Server 2008',
                                      'Operating System :: Microsoft :: Windows :: Windows Vista',
                                      'Operating System :: Microsoft :: Windows :: Windows XP',
                                      'Operating System :: OS Independent',
                                      'Operating System :: OS/2',
                                      'Operating System :: Other OS',
                                      'Operating System :: PDA Systems',
                                      'Operating System :: POSIX',
                                      'Operating System :: POSIX :: AIX',
                                      'Operating System :: POSIX :: BSD',
                                      'Operating System :: POSIX :: BSD :: BSD/OS',
                                      'Operating System :: POSIX :: BSD :: FreeBSD',
                                      'Operating System :: POSIX :: BSD :: NetBSD',
                                      'Operating System :: POSIX :: BSD :: OpenBSD',
                                      'Operating System :: POSIX :: GNU Hurd',
                                      'Operating System :: POSIX :: HP-UX',
                                      'Operating System :: POSIX :: IRIX',
                                      'Operating System :: POSIX :: Linux',
                                      'Operating System :: POSIX :: Other',
                                      'Operating System :: POSIX :: SCO',
                                      'Operating System :: POSIX :: SunOS/Solaris',
                                      'Operating System :: PalmOS',
                                      'Operating System :: RISC OS',
                                      'Operating System :: Unix',
                                      'Operating System :: iOS',
                                      'Programming Language :: APL',
                                      'Programming Language :: ASP',
                                      'Programming Language :: Ada',
                                      'Programming Language :: Assembly',
                                      'Programming Language :: Awk',
                                      'Programming Language :: Basic',
                                      'Programming Language :: C',
                                      'Programming Language :: C#',
                                      'Programming Language :: C++',
                                      'Programming Language :: Cold Fusion',
                                      'Programming Language :: Cython',
                                      'Programming Language :: Delphi/Kylix',
                                      'Programming Language :: Dylan',
                                      'Programming Language :: Eiffel',
                                      'Programming Language :: Emacs-Lisp',
                                      'Programming Language :: Erlang',
                                      'Programming Language :: Euler',
                                      'Programming Language :: Euphoria',
                                      'Programming Language :: F#',
                                      'Programming Language :: Forth',
                                      'Programming Language :: Fortran',
                                      'Programming Language :: Haskell',
                                      'Programming Language :: Java',
                                      'Programming Language :: JavaScript',
                                      'Programming Language :: Kotlin',
                                      'Programming Language :: Lisp',
                                      'Programming Language :: Logo',
                                      'Programming Language :: ML',
                                      'Programming Language :: Modula',
                                      'Programming Language :: OCaml',
                                      'Programming Language :: Object Pascal',
                                      'Programming Language :: Objective C',
                                      'Programming Language :: Other',
                                      'Programming Language :: Other Scripting Engines',
                                      'Programming Language :: PHP',
                                      'Programming Language :: PL/SQL',
                                      'Programming Language :: PROGRESS',
                                      'Programming Language :: Pascal',
                                      'Programming Language :: Perl',
                                      'Programming Language :: Pike',
                                      'Programming Language :: Pliant',
                                      'Programming Language :: Prolog',
                                      'Programming Language :: Python',
                                      'Programming Language :: Python :: 2',
                                      'Programming Language :: Python :: 2 :: Only',
                                      'Programming Language :: Python :: 2.3',
                                      'Programming Language :: Python :: 2.4',
                                      'Programming Language :: Python :: 2.5',
                                      'Programming Language :: Python :: 2.6',
                                      'Programming Language :: Python :: 2.7',
                                      'Programming Language :: Python :: 3',
                                      'Programming Language :: Python :: 3 :: Only',
                                      'Programming Language :: Python :: 3.0',
                                      'Programming Language :: Python :: 3.1',
                                      'Programming Language :: Python :: 3.2',
                                      'Programming Language :: Python :: 3.3',
                                      'Programming Language :: Python :: 3.4',
                                      'Programming Language :: Python :: 3.5',
                                      'Programming Language :: Python :: 3.6',
                                      'Programming Language :: Python :: 3.7',
                                      'Programming Language :: Python :: 3.8',
                                      'Programming Language :: Python :: 3.9',
                                      'Programming Language :: Python :: 3.10',
                                      'Programming Language :: Python :: Implementation',
                                      'Programming Language :: Python :: Implementation :: CPython',
                                      'Programming Language :: Python :: Implementation :: IronPython',
                                      'Programming Language :: Python :: Implementation :: Jython',
                                      'Programming Language :: Python :: Implementation :: MicroPython',
                                      'Programming Language :: Python :: Implementation :: PyPy',
                                      'Programming Language :: Python :: Implementation :: Stackless',
                                      'Programming Language :: R',
                                      'Programming Language :: REBOL',
                                      'Programming Language :: Rexx',
                                      'Programming Language :: Ruby',
                                      'Programming Language :: Rust',
                                      'Programming Language :: SQL',
                                      'Programming Language :: Scheme',
                                      'Programming Language :: Simula',
                                      'Programming Language :: Smalltalk',
                                      'Programming Language :: Tcl',
                                      'Programming Language :: Unix Shell',
                                      'Programming Language :: Visual Basic',
                                      'Programming Language :: XBasic',
                                      'Programming Language :: YACC',
                                      'Programming Language :: Zope',
                                      'Topic :: Adaptive Technologies',
                                      'Topic :: Artistic Software',
                                      'Topic :: Communications',
                                      'Topic :: Communications :: BBS',
                                      'Topic :: Communications :: Chat',
                                      'Topic :: Communications :: Chat :: ICQ',
                                      'Topic :: Communications :: Chat :: Internet Relay Chat',
                                      'Topic :: Communications :: Chat :: Unix Talk',
                                      'Topic :: Communications :: Conferencing',
                                      'Topic :: Communications :: Email',
                                      'Topic :: Communications :: Email :: Address Book',
                                      'Topic :: Communications :: Email :: Email Clients (MUA)',
                                      'Topic :: Communications :: Email :: Filters',
                                      'Topic :: Communications :: Email :: Mail Transport Agents',
                                      'Topic :: Communications :: Email :: Mailing List Servers',
                                      'Topic :: Communications :: Email :: Post-Office',
                                      'Topic :: Communications :: Email :: Post-Office :: IMAP',
                                      'Topic :: Communications :: Email :: Post-Office :: POP3',
                                      'Topic :: Communications :: FIDO',
                                      'Topic :: Communications :: Fax',
                                      'Topic :: Communications :: File Sharing',
                                      'Topic :: Communications :: File Sharing :: Gnutella',
                                      'Topic :: Communications :: File Sharing :: Napster',
                                      'Topic :: Communications :: Ham Radio',
                                      'Topic :: Communications :: Internet Phone',
                                      'Topic :: Communications :: Telephony',
                                      'Topic :: Communications :: Usenet News',
                                      'Topic :: Database',
                                      'Topic :: Database :: Database Engines/Servers',
                                      'Topic :: Database :: Front-Ends',
                                      'Topic :: Desktop Environment',
                                      'Topic :: Desktop Environment :: File Managers',
                                      'Topic :: Desktop Environment :: GNUstep',
                                      'Topic :: Desktop Environment :: Gnome',
                                      'Topic :: Desktop Environment :: K Desktop Environment (KDE)',
                                      'Topic :: Desktop Environment :: K Desktop Environment (KDE) :: Themes',
                                      'Topic :: Desktop Environment :: PicoGUI',
                                      'Topic :: Desktop Environment :: PicoGUI :: Applications',
                                      'Topic :: Desktop Environment :: PicoGUI :: Themes',
                                      'Topic :: Desktop Environment :: Screen Savers',
                                      'Topic :: Desktop Environment :: Window Managers',
                                      'Topic :: Desktop Environment :: Window Managers :: Afterstep',
                                      'Topic :: Desktop Environment :: Window Managers :: Afterstep :: Themes',
                                      'Topic :: Desktop Environment :: Window Managers :: Applets',
                                      'Topic :: Desktop Environment :: Window Managers :: Blackbox',
                                      'Topic :: Desktop Environment :: Window Managers :: Blackbox :: Themes',
                                      'Topic :: Desktop Environment :: Window Managers :: CTWM',
                                      'Topic :: Desktop Environment :: Window Managers :: CTWM :: Themes',
                                      'Topic :: Desktop Environment :: Window Managers :: Enlightenment',
                                      'Topic :: Desktop Environment :: Window Managers :: Enlightenment :: Epplets',
                                      'Topic :: Desktop Environment :: Window Managers :: Enlightenment :: Themes DR15',
                                      'Topic :: Desktop Environment :: Window Managers :: Enlightenment :: Themes DR16',
                                      'Topic :: Desktop Environment :: Window Managers :: Enlightenment :: Themes DR17',
                                      'Topic :: Desktop Environment :: Window Managers :: FVWM',
                                      'Topic :: Desktop Environment :: Window Managers :: FVWM :: Themes',
                                      'Topic :: Desktop Environment :: Window Managers :: Fluxbox',
                                      'Topic :: Desktop Environment :: Window Managers :: Fluxbox :: Themes',
                                      'Topic :: Desktop Environment :: Window Managers :: IceWM',
                                      'Topic :: Desktop Environment :: Window Managers :: IceWM :: Themes',
                                      'Topic :: Desktop Environment :: Window Managers :: MetaCity',
                                      'Topic :: Desktop Environment :: Window Managers :: MetaCity :: Themes',
                                      'Topic :: Desktop Environment :: Window Managers :: Oroborus',
                                      'Topic :: Desktop Environment :: Window Managers :: Oroborus :: Themes',
                                      'Topic :: Desktop Environment :: Window Managers :: Sawfish',
                                      'Topic :: Desktop Environment :: Window Managers :: Sawfish :: Themes 0.30',
                                      'Topic :: Desktop Environment :: Window Managers :: Sawfish :: Themes pre-0.30',
                                      'Topic :: Desktop Environment :: Window Managers :: Waimea',
                                      'Topic :: Desktop Environment :: Window Managers :: Waimea :: Themes',
                                      'Topic :: Desktop Environment :: Window Managers :: Window Maker',
                                      'Topic :: Desktop Environment :: Window Managers :: Window Maker :: Applets',
                                      'Topic :: Desktop Environment :: Window Managers :: Window Maker :: Themes',
                                      'Topic :: Desktop Environment :: Window Managers :: XFCE',
                                      'Topic :: Desktop Environment :: Window Managers :: XFCE :: Themes',
                                      'Topic :: Documentation',
                                      'Topic :: Documentation :: Sphinx',
                                      'Topic :: Education',
                                      'Topic :: Education :: Computer Aided Instruction (CAI)',
                                      'Topic :: Education :: Testing',
                                      'Topic :: Games/Entertainment',
                                      'Topic :: Games/Entertainment :: Arcade',
                                      'Topic :: Games/Entertainment :: Board Games',
                                      'Topic :: Games/Entertainment :: First Person Shooters',
                                      'Topic :: Games/Entertainment :: Fortune Cookies',
                                      'Topic :: Games/Entertainment :: Multi-User Dungeons (MUD)',
                                      'Topic :: Games/Entertainment :: Puzzle Games',
                                      'Topic :: Games/Entertainment :: Real Time Strategy',
                                      'Topic :: Games/Entertainment :: Role-Playing',
                                      'Topic :: Games/Entertainment :: Side-Scrolling/Arcade Games',
                                      'Topic :: Games/Entertainment :: Simulation',
                                      'Topic :: Games/Entertainment :: Turn Based Strategy',
                                      'Topic :: Home Automation',
                                      'Topic :: Internet',
                                      'Topic :: Internet :: File Transfer Protocol (FTP)',
                                      'Topic :: Internet :: Finger',
                                      'Topic :: Internet :: Log Analysis',
                                      'Topic :: Internet :: Name Service (DNS)',
                                      'Topic :: Internet :: Proxy Servers',
                                      'Topic :: Internet :: WAP',
                                      'Topic :: Internet :: WWW/HTTP',
                                      'Topic :: Internet :: WWW/HTTP :: Browsers',
                                      'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
                                      'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries',
                                      'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Content Management System',
                                      'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Message Boards',
                                      'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: News/Diary',
                                      'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Page Counters',
                                      'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Wiki',
                                      'Topic :: Internet :: WWW/HTTP :: HTTP Servers',
                                      'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
                                      'Topic :: Internet :: WWW/HTTP :: Session',
                                      'Topic :: Internet :: WWW/HTTP :: Site Management',
                                      'Topic :: Internet :: WWW/HTTP :: Site Management :: Link Checking',
                                      'Topic :: Internet :: WWW/HTTP :: WSGI',
                                      'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
                                      'Topic :: Internet :: WWW/HTTP :: WSGI :: Middleware',
                                      'Topic :: Internet :: WWW/HTTP :: WSGI :: Server',
                                      'Topic :: Internet :: XMPP',
                                      'Topic :: Internet :: Z39.50',
                                      'Topic :: Multimedia',
                                      'Topic :: Multimedia :: Graphics',
                                      'Topic :: Multimedia :: Graphics :: 3D Modeling',
                                      'Topic :: Multimedia :: Graphics :: 3D Rendering',
                                      'Topic :: Multimedia :: Graphics :: Capture',
                                      'Topic :: Multimedia :: Graphics :: Capture :: Digital Camera',
                                      'Topic :: Multimedia :: Graphics :: Capture :: Scanners',
                                      'Topic :: Multimedia :: Graphics :: Capture :: Screen Capture',
                                      'Topic :: Multimedia :: Graphics :: Editors',
                                      'Topic :: Multimedia :: Graphics :: Editors :: Raster-Based',
                                      'Topic :: Multimedia :: Graphics :: Editors :: Vector-Based',
                                      'Topic :: Multimedia :: Graphics :: Graphics Conversion',
                                      'Topic :: Multimedia :: Graphics :: Presentation',
                                      'Topic :: Multimedia :: Graphics :: Viewers',
                                      'Topic :: Multimedia :: Sound/Audio',
                                      'Topic :: Multimedia :: Sound/Audio :: Analysis',
                                      'Topic :: Multimedia :: Sound/Audio :: CD Audio',
                                      'Topic :: Multimedia :: Sound/Audio :: CD Audio :: CD Playing',
                                      'Topic :: Multimedia :: Sound/Audio :: CD Audio :: CD Ripping',
                                      'Topic :: Multimedia :: Sound/Audio :: CD Audio :: CD Writing',
                                      'Topic :: Multimedia :: Sound/Audio :: Capture/Recording',
                                      'Topic :: Multimedia :: Sound/Audio :: Conversion',
                                      'Topic :: Multimedia :: Sound/Audio :: Editors',
                                      'Topic :: Multimedia :: Sound/Audio :: MIDI',
                                      'Topic :: Multimedia :: Sound/Audio :: Mixers',
                                      'Topic :: Multimedia :: Sound/Audio :: Players',
                                      'Topic :: Multimedia :: Sound/Audio :: Players :: MP3',
                                      'Topic :: Multimedia :: Sound/Audio :: Sound Synthesis',
                                      'Topic :: Multimedia :: Sound/Audio :: Speech',
                                      'Topic :: Multimedia :: Video',
                                      'Topic :: Multimedia :: Video :: Capture',
                                      'Topic :: Multimedia :: Video :: Conversion',
                                      'Topic :: Multimedia :: Video :: Display',
                                      'Topic :: Multimedia :: Video :: Non-Linear Editor',
                                      'Topic :: Office/Business',
                                      'Topic :: Office/Business :: Financial',
                                      'Topic :: Office/Business :: Financial :: Accounting',
                                      'Topic :: Office/Business :: Financial :: Investment',
                                      'Topic :: Office/Business :: Financial :: Point-Of-Sale',
                                      'Topic :: Office/Business :: Financial :: Spreadsheet',
                                      'Topic :: Office/Business :: Groupware',
                                      'Topic :: Office/Business :: News/Diary',
                                      'Topic :: Office/Business :: Office Suites',
                                      'Topic :: Office/Business :: Scheduling',
                                      'Topic :: Other/Nonlisted Topic',
                                      'Topic :: Printing',
                                      'Topic :: Religion',
                                      'Topic :: Scientific/Engineering',
                                      'Topic :: Scientific/Engineering :: Artificial Intelligence',
                                      'Topic :: Scientific/Engineering :: Artificial Life',
                                      'Topic :: Scientific/Engineering :: Astronomy',
                                      'Topic :: Scientific/Engineering :: Atmospheric Science',
                                      'Topic :: Scientific/Engineering :: Bio-Informatics',
                                      'Topic :: Scientific/Engineering :: Chemistry',
                                      'Topic :: Scientific/Engineering :: Electronic Design Automation (EDA)',
                                      'Topic :: Scientific/Engineering :: GIS',
                                      'Topic :: Scientific/Engineering :: Human Machine Interfaces',
                                      'Topic :: Scientific/Engineering :: Hydrology',
                                      'Topic :: Scientific/Engineering :: Image Processing',
                                      'Topic :: Scientific/Engineering :: Image Recognition',
                                      'Topic :: Scientific/Engineering :: Information Analysis',
                                      'Topic :: Scientific/Engineering :: Interface Engine/Protocol Translator',
                                      'Topic :: Scientific/Engineering :: Mathematics',
                                      'Topic :: Scientific/Engineering :: Medical Science Apps.',
                                      'Topic :: Scientific/Engineering :: Physics',
                                      'Topic :: Scientific/Engineering :: Visualization',
                                      'Topic :: Security',
                                      'Topic :: Security :: Cryptography',
                                      'Topic :: Sociology',
                                      'Topic :: Sociology :: Genealogy',
                                      'Topic :: Sociology :: History',
                                      'Topic :: Software Development',
                                      'Topic :: Software Development :: Assemblers',
                                      'Topic :: Software Development :: Bug Tracking',
                                      'Topic :: Software Development :: Build Tools',
                                      'Topic :: Software Development :: Code Generators',
                                      'Topic :: Software Development :: Compilers',
                                      'Topic :: Software Development :: Debuggers',
                                      'Topic :: Software Development :: Disassemblers',
                                      'Topic :: Software Development :: Documentation',
                                      'Topic :: Software Development :: Embedded Systems',
                                      'Topic :: Software Development :: Internationalization',
                                      'Topic :: Software Development :: Interpreters',
                                      'Topic :: Software Development :: Libraries',
                                      'Topic :: Software Development :: Libraries :: Application Frameworks',
                                      'Topic :: Software Development :: Libraries :: Java Libraries',
                                      'Topic :: Software Development :: Libraries :: PHP Classes',
                                      'Topic :: Software Development :: Libraries :: Perl Modules',
                                      'Topic :: Software Development :: Libraries :: Pike Modules',
                                      'Topic :: Software Development :: Libraries :: Python Modules',
                                      'Topic :: Software Development :: Libraries :: Ruby Modules',
                                      'Topic :: Software Development :: Libraries :: Tcl Extensions',
                                      'Topic :: Software Development :: Libraries :: pygame',
                                      'Topic :: Software Development :: Localization',
                                      'Topic :: Software Development :: Object Brokering',
                                      'Topic :: Software Development :: Object Brokering :: CORBA',
                                      'Topic :: Software Development :: Pre-processors',
                                      'Topic :: Software Development :: Quality Assurance',
                                      'Topic :: Software Development :: Testing',
                                      'Topic :: Software Development :: Testing :: Acceptance',
                                      'Topic :: Software Development :: Testing :: BDD',
                                      'Topic :: Software Development :: Testing :: Mocking',
                                      'Topic :: Software Development :: Testing :: Traffic Generation',
                                      'Topic :: Software Development :: Testing :: Unit',
                                      'Topic :: Software Development :: User Interfaces',
                                      'Topic :: Software Development :: Version Control',
                                      'Topic :: Software Development :: Version Control :: Bazaar',
                                      'Topic :: Software Development :: Version Control :: CVS',
                                      'Topic :: Software Development :: Version Control :: Git',
                                      'Topic :: Software Development :: Version Control :: Mercurial',
                                      'Topic :: Software Development :: Version Control :: RCS',
                                      'Topic :: Software Development :: Version Control :: SCCS',
                                      'Topic :: Software Development :: Widget Sets',
                                      'Topic :: System',
                                      'Topic :: System :: Archiving',
                                      'Topic :: System :: Archiving :: Backup',
                                      'Topic :: System :: Archiving :: Compression',
                                      'Topic :: System :: Archiving :: Mirroring',
                                      'Topic :: System :: Archiving :: Packaging',
                                      'Topic :: System :: Benchmark',
                                      'Topic :: System :: Boot',
                                      'Topic :: System :: Boot :: Init',
                                      'Topic :: System :: Clustering',
                                      'Topic :: System :: Console Fonts',
                                      'Topic :: System :: Distributed Computing',
                                      'Topic :: System :: Emulators',
                                      'Topic :: System :: Filesystems',
                                      'Topic :: System :: Hardware',
                                      'Topic :: System :: Hardware :: Hardware Drivers',
                                      'Topic :: System :: Hardware :: Mainframes',
                                      'Topic :: System :: Hardware :: Symmetric Multi-processing',
                                      'Topic :: System :: Hardware :: Universal Serial Bus (USB)',
                                      'Topic :: System :: Hardware :: Universal Serial Bus (USB) :: Audio',
                                      'Topic :: System :: Hardware :: Universal Serial Bus (USB) :: Audio/Video (AV)',
                                      'Topic :: System :: Hardware :: Universal Serial Bus (USB) :: Communications Device Class (CDC)',
                                      'Topic :: System :: Hardware :: Universal Serial Bus (USB) :: Diagnostic Device',
                                      'Topic :: System :: Hardware :: Universal Serial Bus (USB) :: Hub',
                                      'Topic :: System :: Hardware :: Universal Serial Bus (USB) :: Human Interface Device (HID)',
                                      'Topic :: System :: Hardware :: Universal Serial Bus (USB) :: Mass Storage',
                                      'Topic :: System :: Hardware :: Universal Serial Bus (USB) :: Miscellaneous',
                                      'Topic :: System :: Hardware :: Universal Serial Bus (USB) :: Printer',
                                      'Topic :: System :: Hardware :: Universal Serial Bus (USB) :: Smart Card',
                                      'Topic :: System :: Hardware :: Universal Serial Bus (USB) :: Vendor',
                                      'Topic :: System :: Hardware :: Universal Serial Bus (USB) :: Video (UVC)',
                                      'Topic :: System :: Hardware :: Universal Serial Bus (USB) :: Wireless Controller',
                                      'Topic :: System :: Installation/Setup',
                                      'Topic :: System :: Logging',
                                      'Topic :: System :: Monitoring',
                                      'Topic :: System :: Networking',
                                      'Topic :: System :: Networking :: Firewalls',
                                      'Topic :: System :: Networking :: Monitoring',
                                      'Topic :: System :: Networking :: Monitoring :: Hardware Watchdog',
                                      'Topic :: System :: Networking :: Time Synchronization',
                                      'Topic :: System :: Operating System',
                                      'Topic :: System :: Operating System Kernels',
                                      'Topic :: System :: Operating System Kernels :: BSD',
                                      'Topic :: System :: Operating System Kernels :: GNU Hurd',
                                      'Topic :: System :: Operating System Kernels :: Linux',
                                      'Topic :: System :: Power (UPS)',
                                      'Topic :: System :: Recovery Tools',
                                      'Topic :: System :: Shells',
                                      'Topic :: System :: Software Distribution',
                                      'Topic :: System :: System Shells',
                                      'Topic :: System :: Systems Administration',
                                      'Topic :: System :: Systems Administration :: Authentication/Directory',
                                      'Topic :: System :: Systems Administration :: Authentication/Directory :: LDAP',
                                      'Topic :: System :: Systems Administration :: Authentication/Directory :: NIS',
                                      'Topic :: Terminals',
                                      'Topic :: Terminals :: Serial',
                                      'Topic :: Terminals :: Telnet',
                                      'Topic :: Terminals :: Terminal Emulators/X Terminals',
                                      'Topic :: Text Editors',
                                      'Topic :: Text Editors :: Documentation',
                                      'Topic :: Text Editors :: Emacs',
                                      'Topic :: Text Editors :: Integrated Development Environments (IDE)',
                                      'Topic :: Text Editors :: Text Processing',
                                      'Topic :: Text Editors :: Word Processors',
                                      'Topic :: Text Processing',
                                      'Topic :: Text Processing :: Filters',
                                      'Topic :: Text Processing :: Fonts',
                                      'Topic :: Text Processing :: General',
                                      'Topic :: Text Processing :: Indexing',
                                      'Topic :: Text Processing :: Linguistic',
                                      'Topic :: Text Processing :: Markup',
                                      'Topic :: Text Processing :: Markup :: HTML',
                                      'Topic :: Text Processing :: Markup :: LaTeX',
                                      'Topic :: Text Processing :: Markup :: Markdown',
                                      'Topic :: Text Processing :: Markup :: SGML',
                                      'Topic :: Text Processing :: Markup :: VRML',
                                      'Topic :: Text Processing :: Markup :: XML',
                                      'Topic :: Text Processing :: Markup :: reStructuredText',
                                      'Topic :: Utilities   Typing :: Typed']
        self.classifiers_category = {
            'all': '0-773',
            'Development Status': '0-7',
            'Intended Audience': '180-194',
            'Natural Language': '277-336',
            'Environment Console': '7-12',
            'Environment GPU': '12-42',
            'Environment MacOS X': '43-47',
            'Environment X11 Applications': '59-64',
            'Environment': '7-64',
            'Framework AWS CDK': '64-65',
            'Framework Buildout': '73-76',
            'Framework CastleCMS': '76-77',
            'Framework Django': '82-97',
            'Framework Django CMS': '97-103',
            'Framework Jupyter': '108-118',
            'Framework Pelican': '126-129',
            'Framework Plone': '129-144',
            'Framework Sphinx': '155-158',
            'Framework TurboGears': '161-164',
            'Framework Wagtail': '165-168',
            'Framework Zope': '171-176',
            'Framework': '64-180',
            'License OSI Approved': '210-274',
            'License': '194-277',
            'Operating System MacOS': '338-341',
            'Operating System Microsoft': '341-356',
            'Operating System POSIX': '360-374',
            'Operating System': '336-378',
            'Programming Language Python': '420-448',
            'Programming Language': '378-463',
            'Topic Communications': '465-490',
            'Topic Database': '490-493',
            'Topic Desktop Environment': '493-536',
            'Topic Documentation': '536-537',
            'Topic Education': '538-541',
            'Topic Games/Entertainment': '541-553',
            'Topic Internet': '554-581',
            'Topic Multimedia': '581-615',
            'Topic Office/Business': '615-625',
            'Topic Scientific/Engineering': '628-647',
            'Topic Security': '647-648',
            'Topic Sociology': '649-652',
            'Topic Software Development': '652-694',
            'Topic System': '694-748',
            'Topic Terminals': '748-752',
            'Topic Text Editors': '752-758',
            'Topic Text Processing': '758-772',
            'Topic Utilities   Typing': '772-773',
            'Topic': '463-773'
        }
        self.classifiers_category_list = list(self.classifiers_category.keys())
        self.begin = 0
        self.end = len(self.classifiers_available)

    def print_classifiers(self, available=None):
        try:
            if available is None:
                available = self.classifiers_available
            elif available == 'category':
                available = self.classifiers_category_list
                available.sort()
                available.remove('all')
                self.end = len(available)
                print(Fore.GREEN + 'Available Classifiers Category' + Fore.WHITE)
            count = 0
            for i in range(self.begin, self.end):
                if count < 27:
                    print('[' + Fore.GREEN + '+' + Fore.WHITE + '] ' + available[i])
                elif count == 27:
                    print('[' + Fore.GREEN + '+' + Fore.WHITE + '] ' + available[i], end='')
                else:
                    if input() == '':
                        print('[' + Fore.GREEN + '+' + Fore.WHITE + '] ' + available[i].replace('\n', ''), end='')
                    else:
                        sys.exit('')
                count += 1
            print('')
        except KeyboardInterrupt:
            sys.exit('')

    def categorize_classifiers(self, categories=None, wanted=None):
        if categories is not None or categories is list:
            for category in categories:
                if category == 'all':
                    print(Fore.GREEN + "All Classifiers Available" + Fore.WHITE)
                else:
                    print(Fore.GREEN + "Classifiers For " + Fore.WHITE + category.title())
                for i in range(len(self.classifiers_category_list)):
                    if category.lower() == self.classifiers_category_list[i].lower():
                        self.begin, self.end = list(
                            map(int, self.classifiers_category[self.classifiers_category_list[i]].split('-')))
                        break
                if self.begin == 0:
                    for i in range(len(self.classifiers_category_list)):
                        # if category.lower() in self.classifiers_category_list[i].lower():
                        if category.split()[0].lower() == self.classifiers_category_list[i].lower():
                            self.begin, self.end = list(
                                map(int, self.classifiers_category[self.classifiers_category_list[i]].split('-')))
                            break
                self.print_classifiers(available=wanted)
        elif categories is None and wanted is not None:
            self.print_classifiers(available=wanted)


class Setup:
    def __init__(self):
        self.default_content = {'setup_path': os.getcwd() + '\\',
                                'readme_path': os.getcwd() + '\\',
                                'license': '__blank__',
                                'install_requires_(dependencies)(separate_input_using_space)': '__blank__',
                                'classifier': '__blank__',
                                'extras_require': '__blank__',
                                'include_package_data': True,
                                'description': '__blank__',
                                'project_homepage_url': '__blank__',
                                'download_url': '__blank__',
                                'email': '__blank__'
                                }
        self.dict_for_content = {}
        self.classifier_given = []
        self.install_requires = []

    def get_details(self):
        setup_ques = ['Package\nName', 'Version', 'License', 'Description', 'Author\nName',
                      'Email', 'Project\nHomepage URL', 'Download URL', 'README path', 'Requirements\npython requires',
                      'Install requires (dependencies)(separate input using space)']
        for ques in setup_ques:
            input_given = input(ques + " : ")
            try:
                self.dict_for_content[
                    ques.replace(' ', '_').replace('\n', '_').lower()] = input_given if input_given != '' else \
                    self.default_content[ques.replace(' ', '_').replace('\n', '_').lower()]
            except KeyError as error:
                sys.exit(Fore.GREEN + "\n[" + Fore.WHITE + "-" + Fore.GREEN + "] Input for " + Fore.WHITE + str(
                    error).replace('(separate_input_using_space)', '').replace('_',
                                                                               ' ').title() + Fore.GREEN + " is not given. ")

        if self.dict_for_content['install_requires_(dependencies)(separate_input_using_space)'] != '__blank__':
            for dependency in \
                    self.dict_for_content['install_requires_(dependencies)(separate_input_using_space)'].split():
                self.install_requires.append('         "' + dependency + '",\n')

        classifier_input = input('classifiers (separate input using comma) : ').replace(', ', ',').split(',')
        if classifier_input != ['']:
            for i in range(len(classifier_input)):
                self.classifier_given[i] = '        "' + self.classifier_given[i] + '",\n'

        self.dict_for_content['is_your_library_cli_tool_(y/n)'] = input(
            "CLI Tool\nIs your package cli tool (y/n) : ").lower()

        if self.dict_for_content['is_your_library_cli_tool_(y/n)'] == 'y':
            cli_cmd = input('Enter the CLI command [name for the script] : ')
            file_path = input('Enter the module that contains your function [<package>.[<subpackage>.]]<module> : ').replace('/', '.').replace(
                '\\', '.')
            func_name = input('Enter the object you want to invoke [<object>]: ')
            self.dict_for_content[
                'cli'] = "    entry_points={'console_scripts': ['" + cli_cmd + "=" + file_path + ":" + func_name + "']}"

    def print_default(self):
        default_values = list(self.default_content.keys())
        default_values.sort()
        for key in default_values:
            print('[' + Fore.GREEN + '+' + Fore.WHITE + '] ' + Fore.GREEN +
                  key.replace('(separate_input_using_space)', '').replace('_', ' ').title() + ' : ' + Fore.WHITE +
                  str(self.default_content[key]).replace('\\\\', '\\').replace('__blank__', 'None'))

    def writable(self):
        self.get_details()
        setup_content = ['import setuptools\n',
                         '\n',
                         "with open('" +
                         self.dict_for_content['readme_path'].replace('\\',
                                                                      '/') + "README.md', 'r', encoding='utf-8') as fh:\n",
                         '    long_description = fh.read()\n',
                         '\n',
                         'setuptools.setup(\n',
                         "    name='" + self.dict_for_content['package_name'] + "',\n",
                         '    packages=setuptools.find_packages(),\n',
                         "    version='" + self.dict_for_content['version'] + "',\n",
                         "    license='" + self.dict_for_content['license'].upper() + "',\n",
                         "    description='" + self.dict_for_content['description'].title() + "',\n",
                         "    author='" + self.dict_for_content['author_name'].capitalize() + "',\n",
                         "    author_email='" + self.dict_for_content['email'].lower() + "',\n",
                         "    url='" + self.dict_for_content['project_homepage_url'] + "',\n",
                         "    download_url='" + self.dict_for_content['download_url'] + "',\n",
                         '    include_package_data=True,\n',
                         '    long_description=long_description,\n',
                         '    long_description_content_type="text/markdown",\n',
                         "    python_requires='>=" + self.dict_for_content['requirements_python_requires'] + "',\n",
                         ]

        if len(self.classifier_given) > 0:
            setup_content.append('    classifiers=[\n')
            for classifier in self.classifier_given:
                setup_content.append(classifier)
            setup_content.append('    ],\n')

        if len(self.install_requires) > 0:
            setup_content.append('    install_requires=[\n')
            for dependency in self.install_requires:
                setup_content.append(dependency)
            setup_content.append('    ],\n')

        if self.dict_for_content['is_your_library_cli_tool_(y/n)'] == 'y':
            setup_content.append(self.dict_for_content['cli'])
        setup_content.append('\n)\n')

        return setup_content

    def write(self):
        setup_path = input('Enter the path to save setup.py file : ')
        setup_path = setup_path.replace('\\\\', '\\') if setup_path != '' else self.default_content[
            'setup_path'].replace('\\\\', '\\')
        setup_content = self.writable()
        remove_list = []
        for content in setup_content:
            for key in ['__blank__', '__blank', '__empty__', '__empty', '__avoid__', '__avoid']:
                if key in content:
                    remove_list.append(content)

        for key in remove_list:
            if key in setup_content:
                setup_content.remove(key)

        with open(f"{setup_path}/setup.py", 'w') as setup_file:
            setup_file.writelines(setup_content)
        if setup_path[-1] == '\\':
            setup_path = setup_path[:-1]
        print('\n[+] "setup.py" written in path "' + setup_path + '\\setup.py"')


def upload(path, upload_to):
    os.chdir(path)
    os.system("py -m pip install --upgrade build")
    os.system("py -m pip install --upgrade twine")
    os.system("python -m build")
    if upload_to.lower() in ['test', 'test pip']:
        os.system("python -m twine upload --repository testpypi dist/*")
    elif upload_to.lower() in ['real', 'pip', 'real pip']:
        os.system("python -m twine upload dist/*")


def main():
    try:
        option = get_argument()
        setup = Setup()
        if option.print_default:
            setup.print_default()
        elif option.classifier_category:
            Classifiers().categorize_classifiers(wanted='category')
        elif option.avail_classifier:
            option.avail_classifier = option.avail_classifier.replace(', ', ',').split(',')
            Classifiers().categorize_classifiers(categories=option.avail_classifier)
        elif option.classifier:
            option.classifier = option.classifier.replace(', ', ',').split(',')
            Classifiers().categorize_classifiers(categories=option.classifier)
        else:
            setup.write()
    except KeyboardInterrupt:
        print(Fore.GREEN + "\n\n[" + Fore.WHITE + "-" + Fore.GREEN + "] " + Fore.WHITE + "Keyboard Interruption Occurred")
    except Exception as e:
        raise e


def upload_main():
    try:
        option = get_upload_argument()
        upload(option.path, option.upload_to)
    except KeyboardInterrupt:
        print(Fore.GREEN + "\n[" + Fore.WHITE + "-" + Fore.GREEN + "] " + Fore.WHITE + "Keyboard Interruption Occurred")


if __name__ == '__main__':
    pass
    # main()
    # upload_main()