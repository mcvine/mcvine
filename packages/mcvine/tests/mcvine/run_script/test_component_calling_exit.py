import mcvine, mcvine.components
instrument = mcvine.instrument()
# add source
source = mcvine.components.sources.SNS_source('source')
instrument.append(source, position=(0,0,0))
