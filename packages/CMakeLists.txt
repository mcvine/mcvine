# need packages like instrument and sampleassembly
# place them under packages/
include(GitUtils)
UPDATE_PACKAGE_FROM_GIT(
  ${CMAKE_CURRENT_SOURCE_DIR}
  instrument
  https://github.com/danse-inelastic/instrument
  )
UPDATE_PACKAGE_FROM_GIT(
  ${CMAKE_CURRENT_SOURCE_DIR}
  sampleassembly
  https://github.com/danse-inelastic/sampleassembly
)
#
add_subdirectory(instrument)
add_subdirectory(sampleassembly)

# need "click". 
UPDATE_PACKAGE_FROM_GIT(
  ${CMAKE_CURRENT_SOURCE_DIR}
  click
  https://github.com/yxqd/click
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
