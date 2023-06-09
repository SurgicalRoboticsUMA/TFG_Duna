
(cl:in-package :asdf)

(defsystem "first_pkg-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "CameraData" :depends-on ("_package_CameraData"))
    (:file "_package_CameraData" :depends-on ("_package"))
    (:file "Otro" :depends-on ("_package_Otro"))
    (:file "_package_Otro" :depends-on ("_package"))
  ))