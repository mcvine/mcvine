
# ------------- Modify these -------------
set (FPARSER_VERSION "4.5.1")
set ( SRC_FILES 
  homogeneous_scatterer/HomogeneousNeutronScatterer.cc
  math/Fx_fromExpr.cc
  math/random.cc
  math/rootfinding.cc
  math/Functor.cc
  math/misc.cc
  math/random/geometry.cc
  math/random/gaussian.cc
  homogeneous_scatterer/CompositeScatteringKernel.cc
  homogeneous_scatterer/DGSSXResPixel.cc
  kernels/IsotropicKernel.cc
  kernels/detector/EventModeMCA.cc
  kernels/detector/He3.cc
  kernels/detector/He3Tube.cc
  kernels/sample/ConstantEnergyTransferKernel.cc
  kernels/sample/ConstantQEKernel.cc
  kernels/sample/ConstantvQEKernel.cc
  kernels/sample/DGSSXResKernel.cc
  kernels/sample/diffraction/SimplePowderDiffractionKernel.cc
  kernels/sample/SQkernel.cc
  kernels/sample/SQEkernel.cc
  kernels/sample/SQE/GridSQE.cc
  kernels/sample/SQE/SQE_fromexpression.cc
  kernels/sample/phonon/AbstractDispersion_3D.cc
  kernels/sample/phonon/AtomicScatterer.cc
  kernels/sample/phonon/ChangeCoordinateSystem_forDispersion_3D.cc
  kernels/sample/phonon/LinearlyInterpolatedDispersionOnGrid_3D.cc
  kernels/sample/phonon/utils.cc
  physics/statistics.cc
  kernels/sample/phonon/DWFromDOS.cc
  kernels/sample/phonon/CoherentInelastic_PolyXtal.cc
  kernels/sample/phonon/CoherentInelastic_SingleXtal.cc
  kernels/sample/phonon/IncoherentElastic.cc
  kernels/sample/phonon/IncoherentInelastic.cc
  kernels/sample/phonon/IncoherentInelastic_EnergyFocusing.cc
  kernels/sample/phonon/PeriodicDispersion_3D.cc
  kernels/sample/phonon/Omega_minus_deltaE.cc
  kernels/sample/phonon/TargetCone.cc
  )
# ----------------------------------------

# include python headers
include_directories( ${PYTHON_INCLUDE_DIRS} )
include_directories( ${GSL_INCLUDE_DIRS} )

# export headers from this project
file(COPY boostpython_binding homogeneous_scatterer kernels physics
  DESTINATION ${EXPORT_HEADERS}/mccomponents
  FILES_MATCHING PATTERN "*.h" PATTERN "*.icc"
  )
file(COPY math
  DESTINATION ${EXPORT_HEADERS}/mccomponents 
  FILES_MATCHING PATTERN "*.h" PATTERN "*.icc"
  )
file(COPY headers/
  DESTINATION ${EXPORT_HEADERS}/mccomponents FILES_MATCHING PATTERN "*.h" PATTERN "*.icc")

# -I and -L
include_directories(${EXPORT_HEADERS})
include_directories(${DEPLOYMENT_PREFIX}/include)
link_directories(${EXPORT_LIB})
link_directories(${DEPLOYMENT_PREFIX}/${INSTALL_LIB_DIR})
add_definitions(-DUSE_DANSE_NAMESPACE)

# fparser
add_subdirectory("math/fparser-${FPARSER_VERSION}")

# compile shared lib
add_library ( ${LIB_NAME} SHARED ${SRC_FILES} )
target_link_libraries(
  ${LIB_NAME} 
  ${PYTHON_LIBRARY} ${Boost_LIBRARIES} ${GSL_LIBRARIES}
  "journal" "mcni" "mccomposite" "fparser"
  )
set_target_properties(${LIB_NAME} PROPERTIES LIBRARY_OUTPUT_DIRECTORY "${EXPORT_LIB}") # install to python directory
add_dependencies(${LIB_NAME} "mccomposite")

# install shared lib
install (TARGETS ${LIB_NAME}
  LIBRARY DESTINATION ${INSTALL_LIB_DIR}
  )


