# -*- Python -*-
#
#
# Jiao Lin <jiao.lin@gmail.com>
#

from . import mcvine, aliases, click

@mcvine.command()
@click.argument("keyword")
def bash_aliases(keyword):
    """This command prints out the bash function definitions to 
establish aliases of relevant long commands. For example

 $ mcvine bash_aliases arcs

will print out bash functions to define aliases for all arcs related commands.
To put the aliases in use, run

 $ eval `mcvine bash_aliases arcs`
"""
    cmds = []
    for alias, cmd in aliases.iteritems():
        if keyword in alias:
            cmds.append(alias_cmd(alias, cmd))
        continue
    print '\n'.join(cmds)
    return


def alias_cmd(alias, cmd):
    return """%(alias)s () { %(cmd)s "$@"; }""" % locals()

# End of file 
