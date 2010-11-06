#!/usr/bin/env python


import fnmatch
import os


def findTestSources(root='.', like='test*.cc'):
    rt = []
    for root, dirnames, filenames in os.walk(root):
        for filename in fnmatch.filter(filenames, like):
            rt.append(os.path.join(root, filename))
    return rt


def findCorrespondingBinary(src, ext='.cc'):
    assert src.endswith(ext)
    return src[:-len(ext)]


class NoTestBinary(Exception): pass
class TestRunFailed(Exception): pass


import shlex, subprocess

def spawn(cmd, cwd=None, env=None, stdin=None, stdout=None, stderr=None):
    '''spawn a new process

    cmd: the command to execute in the new process
    cwd: the directory where the command will be executed
    env: the environment dictionary
    stdin, stdout, stderr:

    return: new process
    '''
    args = shlex.split(cmd)
    p = subprocess.Popen(args, cwd=cwd, env=env, stdin=stdin, stdout=stdout, stderr=stderr)
    return p


def execute(cmd, input=None, cwd=None, env=None):
    '''execute a command and return the returncode, stdout data, and stderr data
    '''
    print '* executing %s...' % cmd
    p = spawn(
        cmd, cwd=cwd, env=env,
        stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        )
    outdata, errdata = p.communicate(input=input)
    retcode = p.wait()
    return retcode, outdata, errdata



def runtest(src):
    print '* %s' % src
    bin = findCorrespondingBinary(src)
    if not os.path.exists(bin): raise NoTestBinary
    dirname = os.path.dirname(bin)
    fn = os.path.basename(bin)
    cmd = './%s' % (fn,)
    code, out, err = execute(cmd, cwd=dirname)
    if code:
        raise TestRunFailed, '%s failed: out:\n%serr:\n%s' % (
            src, out, err)
    return


def runtests(root='.'):
    sources = findTestSources(root)
    nobinaries = []
    failed = []
    for src in sources:
        try: runtest(src)
        except NoTestBinary:
            nobinaries.append(src)
        except TestRunFailed, e:
            failed.append((src, e))
        continue
    return sources, nobinaries, failed


def createReport(sources, nobinaries, failed):
    print
    print "Report:"
    if not nobinaries and not failed:
        print '* SUCCEED'
        return
    
    npassed = len(sources) - len(nobinaries) - len(failed)
    s = '* Failed. Out of %s tests, %s passed, ' % (len(sources), npassed)
    if nobinaries:
        s += '%s have no test binaries,' % (len(nobinaries),)
    if failed:
        s += '%s failed' % (len(failed),)
    print s
    
    if nobinaries:
        print " - no binaries:"
        for item in nobinaries:
            print item
    
    if failed:
        print " - failed:"
        for src, e in failed:
            print e
    return


def main():
    res = runtests()
    createReport(*res)
    return


if __name__ == '__main__': main()

