cmake_minimum_required(VERSION 3.8)
project(GTK)

set(CMAKE_C_STANDARD 11)

find_package(PkgConfig REQUIRED)
pkg_check_modules(GTK3 REQUIRED gtk+-3.0)

include_directories(${GTK3_INCLUDE_DIRS})
link_directories(${GTK3_LIBRARY_DIRS})

add_definitions(${GTK3_CFLAGS_OTHER})

set(SOURCE_FILES main.c)
add_executable(GTK ${SOURCE_FILES})
TARGET_LINK_LIBRARIES(GTK ${GTK3_LIBRARIES})