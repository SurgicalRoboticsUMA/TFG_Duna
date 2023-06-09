;; Auto-generated. Do not edit!


(when (boundp 'camera_pkg::Otro)
  (if (not (find-package "CAMERA_PKG"))
    (make-package "CAMERA_PKG"))
  (shadow 'Otro (find-package "CAMERA_PKG")))
(unless (find-package "CAMERA_PKG::OTRO")
  (make-package "CAMERA_PKG::OTRO"))
(unless (find-package "CAMERA_PKG::OTROREQUEST")
  (make-package "CAMERA_PKG::OTROREQUEST"))
(unless (find-package "CAMERA_PKG::OTRORESPONSE")
  (make-package "CAMERA_PKG::OTRORESPONSE"))

(in-package "ROS")





(defclass camera_pkg::OtroRequest
  :super ros::object
  :slots (_a ))

(defmethod camera_pkg::OtroRequest
  (:init
   (&key
    ((:a __a) 0)
    )
   (send-super :init)
   (setq _a (round __a))
   self)
  (:a
   (&optional __a)
   (if __a (setq _a __a)) _a)
  (:serialization-length
   ()
   (+
    ;; int64 _a
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int64 _a
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _a (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _a) (= (length (_a . bv)) 2)) ;; bignum
              (write-long (ash (elt (_a . bv) 0) 0) s)
              (write-long (ash (elt (_a . bv) 1) -1) s))
             ((and (class _a) (= (length (_a . bv)) 1)) ;; big1
              (write-long (elt (_a . bv) 0) s)
              (write-long (if (>= _a 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _a s)(write-long (if (>= _a 0) 0 #xffffffff) s)))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int64 _a
#+(or :alpha :irix6 :x86_64)
      (setf _a (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _a (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;;
   self)
  )

(defclass camera_pkg::OtroResponse
  :super ros::object
  :slots ())

(defmethod camera_pkg::OtroResponse
  (:init
   (&key
    )
   (send-super :init)
   self)
  (:serialization-length
   ()
   (+
    0
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;;
   self)
  )

(defclass camera_pkg::Otro
  :super ros::object
  :slots ())

(setf (get camera_pkg::Otro :md5sum-) "019706110004b728d56d8baaa8e32797")
(setf (get camera_pkg::Otro :datatype-) "camera_pkg/Otro")
(setf (get camera_pkg::Otro :request) camera_pkg::OtroRequest)
(setf (get camera_pkg::Otro :response) camera_pkg::OtroResponse)

(defmethod camera_pkg::OtroRequest
  (:response () (instance camera_pkg::OtroResponse :init)))

(setf (get camera_pkg::OtroRequest :md5sum-) "019706110004b728d56d8baaa8e32797")
(setf (get camera_pkg::OtroRequest :datatype-) "camera_pkg/OtroRequest")
(setf (get camera_pkg::OtroRequest :definition-)
      "int64 a
---

")

(setf (get camera_pkg::OtroResponse :md5sum-) "019706110004b728d56d8baaa8e32797")
(setf (get camera_pkg::OtroResponse :datatype-) "camera_pkg/OtroResponse")
(setf (get camera_pkg::OtroResponse :definition-)
      "int64 a
---

")



(provide :camera_pkg/Otro "019706110004b728d56d8baaa8e32797")


