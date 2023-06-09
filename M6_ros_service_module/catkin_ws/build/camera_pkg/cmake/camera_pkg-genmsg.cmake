# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "camera_pkg: 0 messages, 2 services")

set(MSG_I_FLAGS "-Istd_msgs:/opt/ros/noetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(camera_pkg_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/labrob2022/Escritorio/CameraFeature/M6_ros_service_module/catkin_ws/src/camera_pkg/srv/CameraData.srv" NAME_WE)
add_custom_target(_camera_pkg_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "camera_pkg" "/home/labrob2022/Escritorio/CameraFeature/M6_ros_service_module/catkin_ws/src/camera_pkg/srv/CameraData.srv" ""
)

get_filename_component(_filename "/home/labrob2022/Escritorio/CameraFeature/M6_ros_service_module/catkin_ws/src/camera_pkg/srv/UserReq.srv" NAME_WE)
add_custom_target(_camera_pkg_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "camera_pkg" "/home/labrob2022/Escritorio/CameraFeature/M6_ros_service_module/catkin_ws/src/camera_pkg/srv/UserReq.srv" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages

### Generating Services
_generate_srv_cpp(camera_pkg
  "/home/labrob2022/Escritorio/CameraFeature/M6_ros_service_module/catkin_ws/src/camera_pkg/srv/CameraData.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/camera_pkg
)
_generate_srv_cpp(camera_pkg
  "/home/labrob2022/Escritorio/CameraFeature/M6_ros_service_module/catkin_ws/src/camera_pkg/srv/UserReq.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/camera_pkg
)

### Generating Module File
_generate_module_cpp(camera_pkg
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/camera_pkg
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(camera_pkg_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(camera_pkg_generate_messages camera_pkg_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/labrob2022/Escritorio/CameraFeature/M6_ros_service_module/catkin_ws/src/camera_pkg/srv/CameraData.srv" NAME_WE)
add_dependencies(camera_pkg_generate_messages_cpp _camera_pkg_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/labrob2022/Escritorio/CameraFeature/M6_ros_service_module/catkin_ws/src/camera_pkg/srv/UserReq.srv" NAME_WE)
add_dependencies(camera_pkg_generate_messages_cpp _camera_pkg_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(camera_pkg_gencpp)
add_dependencies(camera_pkg_gencpp camera_pkg_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS camera_pkg_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages

### Generating Services
_generate_srv_eus(camera_pkg
  "/home/labrob2022/Escritorio/CameraFeature/M6_ros_service_module/catkin_ws/src/camera_pkg/srv/CameraData.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/camera_pkg
)
_generate_srv_eus(camera_pkg
  "/home/labrob2022/Escritorio/CameraFeature/M6_ros_service_module/catkin_ws/src/camera_pkg/srv/UserReq.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/camera_pkg
)

### Generating Module File
_generate_module_eus(camera_pkg
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/camera_pkg
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(camera_pkg_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(camera_pkg_generate_messages camera_pkg_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/labrob2022/Escritorio/CameraFeature/M6_ros_service_module/catkin_ws/src/camera_pkg/srv/CameraData.srv" NAME_WE)
add_dependencies(camera_pkg_generate_messages_eus _camera_pkg_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/labrob2022/Escritorio/CameraFeature/M6_ros_service_module/catkin_ws/src/camera_pkg/srv/UserReq.srv" NAME_WE)
add_dependencies(camera_pkg_generate_messages_eus _camera_pkg_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(camera_pkg_geneus)
add_dependencies(camera_pkg_geneus camera_pkg_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS camera_pkg_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages

### Generating Services
_generate_srv_lisp(camera_pkg
  "/home/labrob2022/Escritorio/CameraFeature/M6_ros_service_module/catkin_ws/src/camera_pkg/srv/CameraData.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/camera_pkg
)
_generate_srv_lisp(camera_pkg
  "/home/labrob2022/Escritorio/CameraFeature/M6_ros_service_module/catkin_ws/src/camera_pkg/srv/UserReq.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/camera_pkg
)

### Generating Module File
_generate_module_lisp(camera_pkg
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/camera_pkg
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(camera_pkg_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(camera_pkg_generate_messages camera_pkg_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/labrob2022/Escritorio/CameraFeature/M6_ros_service_module/catkin_ws/src/camera_pkg/srv/CameraData.srv" NAME_WE)
add_dependencies(camera_pkg_generate_messages_lisp _camera_pkg_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/labrob2022/Escritorio/CameraFeature/M6_ros_service_module/catkin_ws/src/camera_pkg/srv/UserReq.srv" NAME_WE)
add_dependencies(camera_pkg_generate_messages_lisp _camera_pkg_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(camera_pkg_genlisp)
add_dependencies(camera_pkg_genlisp camera_pkg_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS camera_pkg_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages

### Generating Services
_generate_srv_nodejs(camera_pkg
  "/home/labrob2022/Escritorio/CameraFeature/M6_ros_service_module/catkin_ws/src/camera_pkg/srv/CameraData.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/camera_pkg
)
_generate_srv_nodejs(camera_pkg
  "/home/labrob2022/Escritorio/CameraFeature/M6_ros_service_module/catkin_ws/src/camera_pkg/srv/UserReq.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/camera_pkg
)

### Generating Module File
_generate_module_nodejs(camera_pkg
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/camera_pkg
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(camera_pkg_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(camera_pkg_generate_messages camera_pkg_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/labrob2022/Escritorio/CameraFeature/M6_ros_service_module/catkin_ws/src/camera_pkg/srv/CameraData.srv" NAME_WE)
add_dependencies(camera_pkg_generate_messages_nodejs _camera_pkg_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/labrob2022/Escritorio/CameraFeature/M6_ros_service_module/catkin_ws/src/camera_pkg/srv/UserReq.srv" NAME_WE)
add_dependencies(camera_pkg_generate_messages_nodejs _camera_pkg_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(camera_pkg_gennodejs)
add_dependencies(camera_pkg_gennodejs camera_pkg_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS camera_pkg_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages

### Generating Services
_generate_srv_py(camera_pkg
  "/home/labrob2022/Escritorio/CameraFeature/M6_ros_service_module/catkin_ws/src/camera_pkg/srv/CameraData.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/camera_pkg
)
_generate_srv_py(camera_pkg
  "/home/labrob2022/Escritorio/CameraFeature/M6_ros_service_module/catkin_ws/src/camera_pkg/srv/UserReq.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/camera_pkg
)

### Generating Module File
_generate_module_py(camera_pkg
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/camera_pkg
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(camera_pkg_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(camera_pkg_generate_messages camera_pkg_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/labrob2022/Escritorio/CameraFeature/M6_ros_service_module/catkin_ws/src/camera_pkg/srv/CameraData.srv" NAME_WE)
add_dependencies(camera_pkg_generate_messages_py _camera_pkg_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/labrob2022/Escritorio/CameraFeature/M6_ros_service_module/catkin_ws/src/camera_pkg/srv/UserReq.srv" NAME_WE)
add_dependencies(camera_pkg_generate_messages_py _camera_pkg_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(camera_pkg_genpy)
add_dependencies(camera_pkg_genpy camera_pkg_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS camera_pkg_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/camera_pkg)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/camera_pkg
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(camera_pkg_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/camera_pkg)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/camera_pkg
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(camera_pkg_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/camera_pkg)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/camera_pkg
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(camera_pkg_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/camera_pkg)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/camera_pkg
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(camera_pkg_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/camera_pkg)
  install(CODE "execute_process(COMMAND \"/usr/bin/python3\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/camera_pkg\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/camera_pkg
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(camera_pkg_generate_messages_py std_msgs_generate_messages_py)
endif()
