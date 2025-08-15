#!/usr/bin/env python
#
# Jiao Lin <jiao.lin@gmail.com>
#


from mcni.pyre_support.MpiApplication import Application as base
class App(base):

    class Inventory( base.Inventory ):

        import pyre.inventory
        pass # end of Inventory


    def main(self):
        super(App, self).main()
        from mcni.utils.mpi import world, size, rank, send, receive
        print("in app.main(): mpi world %s, size %s" % (world, size))
        print("mode=%s, rank=%s" % (
            self.inventory.mode, rank))
        
        send(rank, 1-rank, tag=100)
        received = receive(1-rank, tag=100)
        print("my rank: %s, received from %s: %s(%s)" % (
            rank, 1-rank, received, type(received)))
        
        assert 1-rank == received
        assert type(received) == int
        return

    
    def _defaults(self):
        super(App, self)._defaults()
        return


if __name__ == '__main__': App('parallel_app').run()    


# End of file 
