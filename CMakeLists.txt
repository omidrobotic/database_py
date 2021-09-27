cmake_minimum_required(VERSION 3.19)
project(database)

set(CMAKE_CXX_STANDARD 14)

add_executable(database main.cpp)

find_package (SQLite3)
if (SQLITE3_FOUND)
    include_directories(${SQLITE3_INCLUDE_DIRS})
    target_link_libraries (database ${SQLITE3_LIBRARIES})
    target_link_libraries(database sqlite3)

endif (SQLITE3_FOUND)
