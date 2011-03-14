#!/usr/bin/env python


from mcvineui.ScriptBase import ScriptBase as base


class App(base):


    class Inventory(base.Inventory):

        import pyre.inventory

        creator = pyre.inventory.facility('creator', default='instrument-configuration-creator')
        

    def main(self):
        # orm
        clerk = self.inventory.clerk
        orm = clerk.orm

        # instrument
        instrument_configuration = self.inventory.creator.create()
        orm.save(instrument_configuration)
        return


    def _defaults(self):
        super(App, self)._defaults()
        return



def main():
    app = App('create-instrument-configuration')
    app.run()
    return


if __name__ == '__main__': main()
    
