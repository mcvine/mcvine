# need instrument and sampleassembly
# place them under packages/
execute_process(
  COMMAND rm -rf instrument sampleassembly
  WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
  )
execute_process(
  COMMAND git clone https://github.com/danse-inelastic/instrument
  COMMAND git clone https://github.com/danse-inelastic/sampleassembly
  WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
  )
#
add_subdirectory(instrument)
add_subdirectory(sampleassembly)

# need "click". 
execute_process(
  COMMAND rm -rf click
  WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
  )
execute_process(
  COMMAND git clone https://github.com/yxqd/click
  WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
  )
# export click python pkg
file(
  COPY click/click
  DESTINATION ${EXPORT_PYTHON}/
  FILES_MATCHING PATTERN "*.py"
  )

#
add_subdirectory(mcni)
add_subdirectory(mccomposite)
add_subdirectory(mccomponents)
add_subdirectory(mcvine)
add_subdirectory(legacycomponents)


# softwareinstallationinfodb
file(
  COPY softwareinstallationinfodb/softwareinstallationinfodb.dv/
  DESTINATION ${EXPORT_PYTHON}/softwareinstallationinfodb
  FILES_MATCHING PATTERN "*.py"
  )
