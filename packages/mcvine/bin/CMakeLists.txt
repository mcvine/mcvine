#
file(COPY ./ DESTINATION ${EXPORT_BIN}/ 
  FILES_MATCHING PATTERN "mcvine*")

configure_file(setup-mcvine.sh.in ${EXPORT_BIN}/setup-mcvine.sh)
