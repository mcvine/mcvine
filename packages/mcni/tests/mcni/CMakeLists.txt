#

# copy tests to build
file(COPY ./ DESTINATION ${TESTS_DIR}/mcni/mcni/)

# PYUNITTEST_ADD_TEST( ${CMAKE_CURRENT_SOURCE_DIR} "mcvinetest" neutron_TestCase.py )
PYUNITTEST_ADD_TESTS_IN_DIR( ${TESTS_DIR}/mcni/mcni "mcni")