# Install script for directory: /home/labrob2022/Escritorio/CameraFeature/M6_ros_service_module/catkin_ws/src/camera_pkg

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/labrob2022/Escritorio/CameraFeature/M6_ros_service_module/catkin_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/camera_pkg/srv" TYPE FILE FILES
    "/home/labrob2022/Escritorio/CameraFeature/M6_ros_service_module/catkin_ws/src/camera_pkg/srv/CameraData.srv"
    "/home/labrob2022/Escritorio/CameraFeature/M6_ros_service_module/catkin_ws/src/camera_pkg/srv/UserReq.srv"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/camera_pkg/cmake" TYPE FILE FILES "/home/labrob2022/Escritorio/CameraFeature/M6_ros_service_module/catkin_ws/build/camera_pkg/catkin_generated/installspace/camera_pkg-msg-paths.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/labrob2022/Escritorio/CameraFeature/M6_ros_service_module/catkin_ws/devel/include/camera_pkg")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/labrob2022/Escritorio/CameraFeature/M6_ros_service_module/catkin_ws/devel/share/roseus/ros/camera_pkg")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/labrob2022/Escritorio/CameraFeature/M6_ros_service_module/catkin_ws/devel/share/common-lisp/ros/camera_pkg")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/labrob2022/Escritorio/CameraFeature/M6_ros_service_module/catkin_ws/devel/share/gennodejs/ros/camera_pkg")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(COMMAND "/usr/bin/python3" -m compileall "/home/labrob2022/Escritorio/CameraFeature/M6_ros_service_module/catkin_ws/devel/lib/python3/dist-packages/camera_pkg")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python3/dist-packages" TYPE DIRECTORY FILES "/home/labrob2022/Escritorio/CameraFeature/M6_ros_service_module/catkin_ws/devel/lib/python3/dist-packages/camera_pkg")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/labrob2022/Escritorio/CameraFeature/M6_ros_service_module/catkin_ws/build/camera_pkg/catkin_generated/installspace/camera_pkg.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/camera_pkg/cmake" TYPE FILE FILES "/home/labrob2022/Escritorio/CameraFeature/M6_ros_service_module/catkin_ws/build/camera_pkg/catkin_generated/installspace/camera_pkg-msg-extras.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/camera_pkg/cmake" TYPE FILE FILES
    "/home/labrob2022/Escritorio/CameraFeature/M6_ros_service_module/catkin_ws/build/camera_pkg/catkin_generated/installspace/camera_pkgConfig.cmake"
    "/home/labrob2022/Escritorio/CameraFeature/M6_ros_service_module/catkin_ws/build/camera_pkg/catkin_generated/installspace/camera_pkgConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/camera_pkg" TYPE FILE FILES "/home/labrob2022/Escritorio/CameraFeature/M6_ros_service_module/catkin_ws/src/camera_pkg/package.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/camera_pkg" TYPE PROGRAM FILES "/home/labrob2022/Escritorio/CameraFeature/M6_ros_service_module/catkin_ws/build/camera_pkg/catkin_generated/installspace/camera_server.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/camera_pkg" TYPE PROGRAM FILES "/home/labrob2022/Escritorio/CameraFeature/M6_ros_service_module/catkin_ws/build/camera_pkg/catkin_generated/installspace/camera_client.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/camera_pkg" TYPE PROGRAM FILES "/home/labrob2022/Escritorio/CameraFeature/M6_ros_service_module/catkin_ws/build/camera_pkg/catkin_generated/installspace/user_client.py")
endif()

