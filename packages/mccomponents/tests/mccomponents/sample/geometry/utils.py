
def createSampleAssembly(workdir, template_dir, sa_xml):
    """Create a sampleassembly folder in the workdir
    using files in template directory and the given sampleassembly.xml file
    return the path to the new directory
    """
    import tempfile, os, shutil
    d = tempfile.mkdtemp(dir=workdir)
    for fn in os.listdir(template_dir):
        p = os.path.join(template_dir, fn)
        if os.path.isfile(p):
            shutil.copy(p, d)
        continue
    sa_dest = os.path.join(d, 'sampleassembly.xml')
    shutil.copy(sa_xml, sa_dest)
    return sa_dest
