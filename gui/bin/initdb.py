#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2011  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#



"""
initialized database with data objects loaded
"""


from mcvineui.ScriptBase import ScriptBase as base


class DbApp(base):


    class Inventory(base.Inventory):

        import pyre.inventory

        
    def main(self, *args, **kwds):
        db = self.clerk.orm.db
        db.createAllTables()
        return


    def __init__(self):
        base.__init__(self, 'initdb')
        return


def main():
    import journal
    journal.debug('db').activate()
    app = DbApp()
    return app.run()


# main
if __name__ == '__main__':
    # invoke the application shell
    main()


# version
__id__ = "$Id$"

# End of file 
