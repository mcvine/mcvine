#
add_subdirectory(instrument)
add_subdirectory(sampleassembly)
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
