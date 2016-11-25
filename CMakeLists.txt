project(testproj)
cmake_minimum_required(VERSION 3.0)
add_executable(main main.c)
add_executable(helloworld helloworld.c)

add_custom_command(TARGET main POST_BUILD BYPRODUCTS "${CMAKE_CURRENT_BINARY_DIR}/main.dump"
    COMMAND cheri-unknown-freebsd-objdump "-xrsSD" "$<TARGET_FILE:main>" > "${CMAKE_CURRENT_BINARY_DIR}/main.dump"
)

add_custom_command(TARGET helloworld POST_BUILD BYPRODUCTS "${CMAKE_CURRENT_BINARY_DIR}/helloworld.dump"
    COMMAND cheri-unknown-freebsd-objdump "-xrsSD" "$<TARGET_FILE:helloworld>" > "${CMAKE_CURRENT_BINARY_DIR}/helloworld.dump"
)

# message(STATUS "CMAKE_SYSTEM_NAME=${CMAKE_SYSTEM_NAME}")
# get_cmake_property(_variableNames VARIABLES)
# foreach (_variableName ${_variableNames})
#     message(STATUS "${_variableName}=${${_variableName}}")
# endforeach()
