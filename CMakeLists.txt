cmake_minimum_required(VERSION 3.10)
project(MerkleTreeProject)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Сначала библиотека
add_library(MerkleTreeLib
    MerkleTree.cpp
    MerkleTree.h
)

# Затем исполняемый файл
add_executable(MerkleTreeDemo
    main.cpp
)

# Связываем
target_link_libraries(MerkleTreeDemo MerkleTreeLib)

# Директории для заголовков
target_include_directories(MerkleTreeLib PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})