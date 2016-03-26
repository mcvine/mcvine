# need packages like instrument and sampleassembly
# place them under packages/
# first define a macro
macro ( ADD_EXT_PACKAGE _extpkg _giturl)
  IF(EXISTS "${CMAKE_CURRENT_SOURCE_DIR}/${_extpkg}")
    execute_process(
      COMMAND git pull
      WORKING_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}/${_extpkg}"
      )
  ELSE(EXISTS "${CMAKE_CURRENT_SOURCE_DIR}/${_extpkg}")
    execute_process(
      COMMAND git clone ${_giturl}
      WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
      )
  ENDIF(EXISTS "${CMAKE_CURRENT_SOURCE_DIR}/${_extpkg}")
endmacro ( ADD_EXT_PACKAGE )
# end use it for ext packages
ADD_EXT_PACKAGE(instrument https://github.com/danse-inelastic/instrument)
ADD_EXT_PACKAGE(sampleassembly https://github.com/danse-inelastic/sampleassembly)
#
add_subdirectory(instrument)
add_subdirectory(sampleassembly)

# need "click". 
ADD_EXT_PACKAGE(click https://github.com/yxqd/click)
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
