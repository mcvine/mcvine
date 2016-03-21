# -*- Python -*-
#
# Jiao Lin <jiao.lin@gmail.com>
#

import click, os, json, subprocess as sp

# decorator to allow a cmd to save cmd parameters 
# for data provenance purpose
def save_metadata(f):
    from mcvine import version, git_revision
    mcvine_vers = dict(version=version, git_revision=git_revision)
    def _(*args, **kwds):
        c = click.get_current_context()
        cmdpath = c.command_path
        # clean parameter dictionary
        import copy
        params = copy.deepcopy(c.params)
        del params['save_metadata_only']; del params['keep_in_cache']
        # construct metadata
        metadata = dict(
            cmd=cmdpath, params=params, args=c.args,
            mcvine=mcvine_vers)
        # output path
        fn = cmdpath.replace(' ', '-') + ".params"
        # save
        json.dump(metadata, open(fn, 'wt'))
        # run the cmd only if we are not just saving meta data
        save_metadata_only = kwds.pop('save_metadata_only', None)
        # no need to continue if the only request is to save metadata
        if save_metadata_only: return
        #
        keep_in_cache = kwds.pop('keep_in_cache', None)
        if not keep_in_cache:
            return f(*args, **kwds)
        # run the command in the subprocess so that we
        # can make sure it is finished before moving on to
        # the next step
        cmd = "%s %s" % (cmdpath, arg_str(params, c.args))
        ret = sp.call(cmd, shell=True)
        if ret:
            raise RuntimeError("%s failed" % cmd)
        # add output to cache
        path = cache_path(cmdpath, params, c.args)
        if not os.path.exists(path):
            os.makedirs(path)
        # XXX assume the current working directory is the output directory
        out = "."
        # XXX this is not portable, but should be OK for the systems
        # XXX we support
        cmd = 'cp -al %s "%s"' % (out, path)
        ret = sp.call(cmd, shell=True)
        if ret:
            raise RuntimeError("%s failed" % cmd)
        return
    _.__name__ = f.__name__
    _.__doc__ = f.__doc__
    return click.option("--keep-in-cache", is_flag=True)(
        click.option("--save-metadata-only", is_flag=True)
        (_)
    )


def arg_str(params, args):
    "create unique arg str from given params and args"
    plist = sorted([ '%s=%s' % (k,v) for k, v in params.iteritems() ])
    pstr = ' '.join(params)
    args = sorted(args)
    astr = ' '.join(args)
    return "%s %s" % (pstr, astr)


def unique_identifier(params, args):
    "create a unique string identifier of the given parameters and arguments"
    s = arg_str(params, args)
    import hashlib
    return hashlib.md5(s).hexdigest()


def cache_path(cmdpath, params, args):
    uid = unique_identifier(params, args)
    parts = [app_cache_root] + cmdpath.split() + [uid]
    return os.path.join(*parts)
    

app_cache_root = os.path.join(os.path.expanduser('~'), '.mcvine', 'app-cache')

# End of file 
