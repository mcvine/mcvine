# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2010  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


"""
The purpose of this module is to provide a way to configure some parameters
of pyre application that are not settable through inventory.
The machinary of inventory only kicks in only after the pyre framework
applies  the configurations. Therefore, there are some parameters (common)
of pyre applications that cannot be easily settable. For example, the
list of depositories (which actually can be set thru inventory.local).
Here we create a way to make these kind of things configurable.
The cli of the script using this machinery would be something like

  <app> -config=dir1,dir2,...  --- -greetings=aloha ...more-normal-options...

The string --- is the separator.
The options before the separator are the configuration of superapp, while
those after the separator are normal options of the application wrapped.
"""



from pyre.applications.Script import Script

class SuperAppBase(Script):

    # signature for inventory items that are for "super-app"
    inventory_item_signature = 'for-superapp'

    def main(self):
        kwds = self._getOptions()
        self._setApplicationCommandLineOptions()
        self.runApp(**kwds)
        return


    def runApp(self, **kwds):
        raise NotImplementedError


    def __init__(self, *args, **kwds):
        super(SuperAppBase, self).__init__(*args, **kwds)
        self._setSuperApplicationCommandLineOptions()
        return


    def _getOptions(self):
        kwds = {}
        # signature of properties for the super app
        sig = self.inventory_item_signature
        for name in self.inventory.propertyNames():
            trait = self.inventory.getTrait(name)
            # only need traits that have the right signature
            if not trait.meta.get(sig):
                continue
            value = self.inventory.getTraitValue(name)
            kwds[name] = value
            continue
        return kwds


    def _setApplicationCommandLineOptions(self):

        err = 'separator --- is needed to separate super app args and app args'

        argv = self.sysargv
        import sys
        if not argv:
            argv = sys.argv
        # no real argument, nothing to do
        if len(argv) == 1: return
        
        arg0 = argv[0]
        try:
            index = argv.index('---')
        except ValueError:
            # this means the arguments are either all for the super
            # app or the app.
            opts = self._getOptions()
            names = opts.keys()
            if _argName(argv[1]) in names:
                for arg in argv[2:]:
                    assert _argName(arg) in names, err
                index = len(argv) - 1
            else:
                for arg in argv[2:]:
                    assert _argName(arg) not in names, err
                index = 0

        argv = [arg0] + argv[index+1:]
        sys.argv = argv
        return


    def _setSuperApplicationCommandLineOptions(self):
        # this is only called in __init__
        self.sysargv = None
        import sys
        argv = sys.argv
        try:
            index = argv.index('---')
        except:
            return
        self.sysargv = sys.argv
        sys.argv = sys.argv[:index]
        return


def _argName(arg):
    arg = arg.lstrip('-')
    i = arg.find('=')
    if i != -1: return arg[:i]
    return arg


# version
__id__ = "$Id$"

# End of file 
