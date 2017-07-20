# -*- Python -*-
#
# Jiao Lin <jiao.lin@gmail.com>
#

import click, os, json, subprocess as sp
import logging
logger = logging.getLogger("mcvine.cli")


provenance_opts = [
    'save_metadata_only', # do not really run the cmd, just save the meta data
    'keep_in_cache',      # keep results in the cache
    'use_cache',          # use results from cache if exist
    ]

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
        for popt in provenance_opts: del params[popt]
        # deal with option --use-cache
        use_cache = kwds.pop('use_cache', None)
        save_metadata_only = kwds.pop('save_metadata_only', None)
        if use_cache and not save_metadata_only:
            path = cache_path(cmdpath, params, c.args)
            if os.path.exists(path):
                # if requested to use cache and the cache exists,
                # use it.
                logger.info("%s already exists. reuse results there" % path)
                # XXX assume the current working directory is the output directory
                out = "."
                copy_withhardlinks(path,out)
                return
        # deal with --save-metadata-only
        # construct metadata
        metadata = dict(
            cmd=cmdpath, params=params, args=c.args,
            mcvine=mcvine_vers)
        # output path
        fn = cmdpath.replace(' ', '-') + ".params"
        # save
        json.dump(metadata, open(fn, 'wt'))
        # run the cmd only if we are not just saving meta data
        # no need to continue if the only request is to save metadata
        if save_metadata_only: return
        # deal with option --keep-in-cache
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
        copy_withhardlinks(out, path)
        return
    _.__name__ = f.__name__
    _.__doc__ = f.__doc__
    d1 = click.option("--save-metadata-only", is_flag=True)
    d2 = click.option("--keep-in-cache", is_flag=True)
    d3 = click.option("--use-cache", is_flag=True)
    return d1(d2(d3(_)))


def copy_withhardlinks(src, dest):
    # XXX this is not portable, but should be OK for the systems
    # XXX we support
    cmd = 'cp -r --preserve=all -l "%s/"* "%s/"' % (src, dest)
    ret = sp.call(cmd, shell=True)
    if ret:
        raise RuntimeError("%s failed" % cmd)
    return


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
