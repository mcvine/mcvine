# need GSL
# NOTE: we are using FindGSL in "cmake_utils" of danse-inelastic
# NOTE: cmake 3.2 has a built-in FindGSL, should switcht to that
# NOTE: in the future.
find_package(GSL REQUIRED)
# NOTE: the builtin FindGSL use GSL_INCLUDE_DIRS instead of GSL_INCLUDE_DIR
# NOTE: so for future compatibility we define GSL_INCLUDE_DIRS here.
set (GSL_INCLUDE_DIRS ${GSL_INCLUDE_DIR})
message(" - GSL libs: ${GSL_LIBRARIES}")
message(" - GSL header dirs: ${GSL_INCLUDE_DIRS}")

# need packages like instrument and sampleassembly
# place them under packages/
include(GitUtils)
UPDATE_PACKAGE_FROM_GIT(
  ${CMAKE_CURRENT_SOURCE_DIR}
  instrument
  https://github.com/danse-inelastic/instrument
  )
add_subdirectory(instrument)
UPDATE_PACKAGE_FROM_GIT(
  ${CMAKE_CURRENT_SOURCE_DIR}
  sampleassembly
  https://github.com/danse-inelastic/sampleassembly
)
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
