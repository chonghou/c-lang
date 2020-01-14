cmake_minimum_required (VERSION 2.6)
project (signal_stu)
#设置源文件
aux_source_directory(. dir_srcs)
#设置可执行程序
add_executable(signal ${dir_srcs})