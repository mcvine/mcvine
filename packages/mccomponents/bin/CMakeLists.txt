#
# configure_file(mcvine-debye-waller-core-from-phonon-dos mcvine-debye-waller-core-from-phonon-dos)
file(COPY ./ DESTINATION ${EXPORT_BIN}/ 
  FILES_MATCHING PATTERN "mcvine-*")
