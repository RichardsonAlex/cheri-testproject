project(testproj)
cmake_minimum_required(VERSION 3.0)
add_compile_options(-O0)
# I doubt this makes a difference but cheriabitest does it:
add_compile_options(-ftls-model=local-exec)

# Make the binaries smaller:
# add_compile_options(-fdata-sections -ffunction-sections)
# set(CMAKE_EXE_LINKER_FLAGS "${CMAKE_EXE_LINKER_FLAGS} -Wl,--gc-sections -Wl,--print-gc-sections")

add_executable(main main.c)
add_executable(helloworld helloworld.c)
add_executable(very-simple very-simple.c)
target_compile_options(very-simple PUBLIC -nostdlib)
set_target_properties(very-simple PROPERTIES LINK_FLAGS -nostdlib)


function(create_dump target)
    add_custom_command(TARGET ${target} POST_BUILD BYPRODUCTS "${CMAKE_CURRENT_BINARY_DIR}/${target}.dump" "${CMAKE_CURRENT_BINARY_DIR}/${target}.nodebug"
    COMMAND cheri-unknown-freebsd-objcopy --strip-debug "$<TARGET_FILE:${target}>" "${CMAKE_CURRENT_BINARY_DIR}/${target}.nodebug"
    COMMAND cheri-unknown-freebsd-objdump "-xrsSdl" "${CMAKE_CURRENT_BINARY_DIR}/${target}.nodebug" > "${CMAKE_CURRENT_BINARY_DIR}/${target}.dump"
    COMMAND cheri-unknown-freebsd-objdump "-xrsSdl" "$<TARGET_FILE:${target}>" > "${CMAKE_CURRENT_BINARY_DIR}/${target}.dump.full"
)
endfunction()

create_dump(main)
create_dump(helloworld)
create_dump(very-simple)

# message(STATUS "CMAKE_SYSTEM_NAME=${CMAKE_SYSTEM_NAME}")
# get_cmake_property(_variableNames VARIABLES)
# foreach (_variableName ${_variableNames})
#     message(STATUS "${_variableName}=${${_variableName}}")
# endforeach()
