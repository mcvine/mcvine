# set up symlinks in sample assemblies
from mcvine.deployment_info import mcvine_resources
if mcvine_resources:
    sa = "sampleassemblies"
    import os
    dst = os.path.join(sa, "Al-simplepowderdiffractionkernel", "aluminum")
    src = os.path.join(mcvine_resources, "samples", "Al", '300K')
    if not os.path.exists(dst):
        os.symlink(src, dst)
        pass
    
    pass
