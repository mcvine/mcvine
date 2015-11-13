# DEVELOPER NOTES:
# !!! Make.mm files in subdir boostpython_binding
# !!! are not yet converted to cmake files.

# ------------- Modify these -------------
set ( SRC_FILES 
  math/geometry/test_choose_direction.cc
  math/random/test_gaussian.cc
  math/random/test_gaussian_gsl.cc
  math/test_fparser.cc
  math/test_random.cc
  math/test_rootfinding.cc
  math/test_Fx_fromExpr.cc
  math/test_Fxyz_fromExpr.cc
  homogeneous_scatterer/testHomogeneousNeutronScatterer.cc
  homogeneous_scatterer/testCompositeScatteringKernel.cc
  homogeneous_scatterer/testMultipleScattering.cc
  kernels/detector/testTof2Channel.cc
  kernels/detector/testZ2Channel.cc
  kernels/detector/testHe3Tube.cc
  kernels/detector/testEventModeMCA.cc
  kernels/detector/testHe3.cc
  kernels/detector/testevents2iqe.cc
  kernels/sample/test_Broadened_E_Q_Kernel.cc
  kernels/sample/test_E_Q_Kernel.cc
  kernels/sample/test_E_vQ_Kernel.cc
  kernels/sample/test_SQkernel.cc
  kernels/sample/test_SQAdaptor.cc
  kernels/sample/test_SQE_fromexpression.cc
  kernels/sample/test_SvQ_fromexpression.cc
  kernels/sample/diffraction/test_SimplePowderDiffractionKernel.cc
  kernels/sample/phonon/test_LinearlyInterpolatedGridData_3D.cc
  kernels/sample/phonon/test_LinearlyInterpolatedPolarizationOnGrid_3D.cc
  kernels/sample/phonon/test_LinearlyInterpolatedDispersionOnGrid_3D.cc
  kernels/sample/phonon/test_LinearlyInterpolatedGridData_1D.cc
  kernels/sample/phonon/test_LinearlyInterpolatedDOS.cc
  kernels/sample/phonon/test_CoherentInelastic_PolyXtal.cc
  kernels/sample/phonon/test_CoherentInelastic_SingleXtal.cc
  kernels/sample/phonon/test_PeriodicDispersion_3D.cc
  kernels/sample/phonon/test_ChangeCoordinateSystem_forDispersion_3D.cc
  kernels/sample/phonon/test_interpolation.cc
  kernels/sample/phonon/test_DWFromDOS.cc
  )
# ----------------------------------------

# -I and -L
include_directories(${EXPORT_HEADERS})
include_directories(${DEPLOYMENT_PREFIX}/include)
include_directories(${PYTHON_INCLUDE_DIRS})
include_directories(${GLS_INCLUDE_DIR})
link_directories(${EXPORT_LIB})
link_directories(${DEPLOYMENT_PREFIX}/${INSTALL_LIB_DIR})
add_definitions(-DUSE_DANSE_NAMESPACE)

# compile executable
foreach( _src ${SRC_FILES} )
  get_filename_component( _filename ${_src} NAME )
  get_filename_component( _exe ${_src} NAME_WE )
  get_filename_component( _directory ${_src} DIRECTORY )
  set(_target ${_directory}/${_exe})
  file(MAKE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/${_directory})
  add_executable(${_target} ${_src})
  target_link_libraries(
    ${_target} ${PYTHON_LIBRARY} ${Boost_LIBRARIES} ${GSL_LIBRARIES}
    "journal" "danse_ins_bpext" "mcni" "mccomposite" "fparser"
    -l"${LIB_NAME}"
    )
  set(_testname ${_src})
  add_test(
    NAME lib${PACKAGE_NAME}/${_testname} 
    COMMAND ${_target} 
    WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
    )
endforeach( _src ${SRC_FILES} ) 

