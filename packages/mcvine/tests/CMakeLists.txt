#
# copy tests to build
file(COPY ./ DESTINATION ${TESTS_DIR}/mcvine/)

# add python tests
PYUNITTEST_ADD_TESTS_IN_DIR( ${TESTS_DIR}/mcvine "mcvine")
