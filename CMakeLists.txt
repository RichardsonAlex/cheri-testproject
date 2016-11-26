project(testproj)
cmake_minimum_required(VERSION 3.0)
add_compile_options(-O0)
# I doubt this makes a difference but cheriabitest does it:
add_compile_options(-ftls-model=local-exec)
add_executable(main main.c)
add_executable(helloworld helloworld.c)


function(create_dump target)
    add_custom_command(TARGET ${target} POST_BUILD BYPRODUCTS "${CMAKE_CURRENT_BINARY_DIR}/${target}.dump" "${CMAKE_CURRENT_BINARY_DIR}/${target}.nodebug"
    COMMAND cheri-unknown-freebsd-objcopy --strip-debug "$<TARGET_FILE:${target}>" "${CMAKE_CURRENT_BINARY_DIR}/${target}.nodebug"
    COMMAND cheri-unknown-freebsd-objdump "-xrsSdTt" "${CMAKE_CURRENT_BINARY_DIR}/${target}.nodebug" > "${CMAKE_CURRENT_BINARY_DIR}/${target}.dump"
)
endfunction()

create_dump(main)
create_dump(helloworld)

# message(STATUS "CMAKE_SYSTEM_NAME=${CMAKE_SYSTEM_NAME}")
# get_cmake_property(_variableNames VARIABLES)
# foreach (_variableName ${_variableNames})
#     message(STATUS "${_variableName}=${${_variableName}}")
# endforeach()
