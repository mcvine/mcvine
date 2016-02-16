# -*- Python -*-
#
#
# Jiao Lin <jiao.lin@gmail.com>
#

from . import mcvine, click

@mcvine.group()
def bash():
    return

@bash.command()
def complete():
    "Instructions for bash complete support"
    print """
To enable bash auto complete for mcvine command, run

 $ eval "$(_MCVINE_COMPLETE=source mcvine)"

"""
    return


alias_help = """build bash aliases of long mcvine commands

This command prints out the bash function definitions to 
establish aliases of relevant long commands. For example

 $ mcvine bash_aliases arcs

will print out bash functions to define aliases for all arcs related commands.
To put the aliases in use, run

 $ eval `mcvine bash_aliases arcs`
"""
@bash.command(help=alias_help)
@click.argument("keyword", default="")
@click.pass_context
def aliases(ctx, keyword):
    if not keyword:
        click.echo(ctx.get_help(), color=ctx.color)
        return
    cmds = []
    from .  import aliases
    for alias, cmd in aliases.iteritems():
        if keyword=='all' or keyword in alias:
            cmds.append(alias_cmd(alias, cmd))
        continue
    print '\n'.join(cmds)
    return


def alias_cmd(alias, cmd):
    return """%(alias)s () { %(cmd)s "$@"; };""" % locals()

# End of file 
