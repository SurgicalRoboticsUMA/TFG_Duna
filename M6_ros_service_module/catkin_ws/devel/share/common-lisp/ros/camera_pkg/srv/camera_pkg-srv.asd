
(cl:in-package :asdf)

(defsystem "camera_pkg-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "CameraData" :depends-on ("_package_CameraData"))
    (:file "_package_CameraData" :depends-on ("_package"))
    (:file "UserReq" :depends-on ("_package_UserReq"))
    (:file "_package_UserReq" :depends-on ("_package"))
  ))