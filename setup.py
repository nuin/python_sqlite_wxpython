
# ======================================================#
# File automagically generated by GUI2Exe version 0.1
# Andrea Gavana, 31 March 2007
# ======================================================#

# Let's start with some default (for me) imports...

from distutils.core import setup
import glob
import os
import sys

if not sys.platform == 'darwin':
    import py2exe
else:
    import py2app


manifest_template = """
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<assembly xmlns="urn:schemas-microsoft-com:asm.v1" manifestVersion="1.0">
<assemblyIdentity
    version="5.0.0.0"
    processorArchitecture="x86"
    name="modelpieWIN"
    type="win32"
/>
<description>modelpieWIN Program</description>
<dependency>
    <dependentAssembly>
        <assemblyIdentity
            type="win32"
            name="Microsoft.Windows.Common-Controls"
            version="6.0.0.0"
            processorArchitecture="X86"
            publicKeyToken="6595b64144ccf1df"
            language="*"
        />
    </dependentAssembly>
</dependency>
</assembly>
"""

class Target(object):
    """ A simple class that holds information on our executable file. """
    def __init__(self, **kw):
        """ Default class constructor. Update as you need. """
        self.__dict__.update(kw)
        # for the versioninfo resources
        self.version = "1.01"
        self.company_name = "Paulo Nuin"
        self.copyright = "Paulo Nuin"
        self.name = "bacs"


# Ok, let's explain why I am doing that.
# Often, data_files, excludes and dll_excludes (but also resources)
# can be very long list of things, and this will clutter too much
# the setup call at the end of this file. So, I put all the big lists
# here and I wrap them using the textwrap module.

data_files = ['samples.db']

includes = []
excludes = ['Tkconstants', 'Tkinter', '_gtkagg', '_tkagg', 'bsddb',
            'curses', 'email', 'pywin.debugger', 'pywin.debugger.dbgcon',
            'pywin.dialogs', 'tcl']
packages = []
dll_excludes = ['libgdk-win32-2.0-0.dll', 'libgobject-2.0-0.dll', 'tcl84.dll',
                'tk84.dll']
icon_resources = []
bitmap_resources = []
other_resources = [(24, 1, manifest_template)]


# This is a place where the user custom code may go. You can do almost
# whatever you want, even modify the data_files, includes and friends
# here as long as they have the same variable name that the setup call
# below is expecting.

# No custom code added


# Ok, now we are going to build our target class.
# I chose this building strategy as it works perfectly for me :-D

test_wx = Target(
    # what to build
    script = "bac_form.py",
    icon_resources = icon_resources,
    bitmap_resources = bitmap_resources,
    other_resources = other_resources
    )


# That's serious now: we have all (or almost all) the options py2exe
# supports. I put them all even if some of them are usually defaulted
# and not used. Some of them I didn't even know about.
if not sys.platform == 'darwin': 
    setup(

        data_files = data_files,

        options = {"py2exe": {"compressed": 0, 
                              "optimize": 0,
                              "includes": includes,
                              "excludes": excludes,
                              "packages": packages,
                              "dll_excludes": dll_excludes,
                              "bundle_files": 1,
                              "dist_dir": "dist",
                              "xref": False,
                              "skip_archive": False,
                              "ascii": False,
                              "custom_boot_script": '',
                             }
                  },

        zipfile = None,
        windows = [test_wx]
    
        )
else:
    setup(
        options=dict(
            py2app=dict(
                iconfile='',
                packages='wx',
                site_packages=False,
                excludes=excludes,
                resources=['db.txt', 'db_obj.py'],
                plist=dict(
                    CFBundleName               = "Bac",
                    CFBundleShortVersionString = "0.0.1",     # must be in X.X.X format
                    CFBundleGetInfoString      = "Bac 0.0.1",
                    CFBundleExecutable         = "Bac",
                    CFBundleIdentifier         = "com.example.bac",
                ),
            ),
        ),
        app=[ 'bac_form.py' ]
    )
    

