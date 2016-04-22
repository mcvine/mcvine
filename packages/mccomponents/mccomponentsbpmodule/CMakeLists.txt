# ------------- Modify these -------------
set (PYBINDING_NAME "${PACKAGE_NAME}bpmodule")
set ( SRC_FILES 
  ${PYBINDING_NAME}.cc
  wrap_basic_containers.cc
  wrap_HomogeneousNeutronScatterer.cc
  wrap_AbstractScatteringKernel.cc
  wrap_CompositeScatteringKernel.cc
  wrap_kernelcontainer.cc
  wrap_He3TubeKernel.cc
  wrap_EventModeMCA.cc
  wrap_ConstantEnergyTransferKernel.cc
  wrap_ConstantQEKernel.cc
  wrap_ConstantvQEKernel.cc
  wrap_E_Q_Kernel.cc
  wrap_E_vQ_Kernel.cc
  wrap_Broadened_E_Q_Kernel.cc
  wrap_SQEkernel.cc
  wrap_SQkernel.cc
  wrap_GridSQE.cc
  wrap_SQE_fromexpression.cc
  wrap_IsotropicKernel.cc
  wrap_AtomicScatterer.cc
  wrap_NdArray.cc
  wrap_AbstractDOS.cc
  wrap_LinearlyInterpolatedDOS.cc
  wrap_AbstractDebyeWallerFactorCalculator.cc
  wrap_DWFromDOS.cc
  wrap_LinearlyInterpolatableAxis.cc
  wrap_epsilon_t.cc
  wrap_AbstractDispersion_3D.cc
  wrap_PeriodicDispersion_3D.cc
  wrap_ChangeCoordinateSystem_forDispersion_3D.cc
  wrap_LinearlyInterpolatedDispersionOnGrid_3D.cc
  wrap_Phonon_IncoherentElastic_kernel.cc
  wrap_Phonon_IncoherentInelastic_kernel.cc
  wrap_Phonon_CoherentInelastic_PolyXtal_kernel.cc
  wrap_Phonon_CoherentInelastic_SingleXtal_kernel.cc
  wrap_rootsfinders.cc
  wrap_targetregion.cc
  wrap_RandomNumberGenerator.cc
  wrap_SimplePowderDiffractionKernel.cc
  )
# ----------------------------------------

# alias
set ( MOD_NAME ${PYBINDING_NAME} )

# -I and -L
include_directories(${EXPORT_HEADERS})
include_directories(${DEPLOYMENT_PREFIX}/include)
include_directories(${PYTHON_INCLUDE_DIRS})
include_directories(${Boost_INCLUDE_DIRS})
link_directories(${EXPORT_LIB})
link_directories(${DEPLOYMENT_PREFIX}/${INSTALL_LIB_DIR})
add_definitions(-DUSE_DANSE_NAMESPACE)

# compile shared library
add_library(${MOD_NAME} SHARED ${SRC_FILES})
target_link_libraries(${MOD_NAME} ${PYTHON_LIBRARY} ${Boost_LIBRARIES} "journal" "mcni" "mccomposite" ${LIB_NAME})
set_target_properties(${MOD_NAME} PROPERTIES PREFIX "") # dont need "lib" prefix
set_target_properties(${MOD_NAME} PROPERTIES LIBRARY_OUTPUT_DIRECTORY "${EXPORT_PYTHON}/${PKG_NAME}") # export to python directory
set_target_properties(${MOD_NAME} PROPERTIES SKIP_BUILD_RPATH "ON")
add_dependencies(${MOD_NAME} ${LIB_NAME})
