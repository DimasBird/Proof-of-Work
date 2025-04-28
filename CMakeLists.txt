cmake_minimum_required(VERSION 3.10)
project(MerkleTreeProject)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)

# Добавляем GoogleTest
add_subdirectory(googletest)  # Предполагая, что googletest находится в вашем проекте

if(MSVC)
    # Для динамической CRT
    set(CMAKE_MSVC_RUNTIME_LIBRARY "MultiThreaded$<$<CONFIG:Debug>:Debug>DLL")
    
    # ИЛИ для статической
    #set(CMAKE_MSVC_RUNTIME_LIBRARY "MultiThreaded$<$<CONFIG:Debug>:Debug>")
endif()

add_library(MerkleTreeLib
    MerkleTree.cpp
    MerkleTree.h
)

add_library(HashFunctionLib
    HashFunction.cpp
    HashFunction.h
)

add_executable(Main
    main.cpp
)

add_executable(Tests
    tests.cpp
)

# Связываем
target_link_libraries(Main MerkleTreeLib HashFunctionLib)
target_link_libraries(Tests 
    MerkleTreeLib 
    HashFunctionLib
    gtest_main
)

# Директории для заголовков
target_include_directories(MerkleTreeLib PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
target_include_directories(HashFunctionLib PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
target_include_directories(Tests PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/googletest/googletest/include)

