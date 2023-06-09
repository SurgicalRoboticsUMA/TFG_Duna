;; Auto-generated. Do not edit!


(when (boundp 'camera_pkg::UserReq)
  (if (not (find-package "CAMERA_PKG"))
    (make-package "CAMERA_PKG"))
  (shadow 'UserReq (find-package "CAMERA_PKG")))
(unless (find-package "CAMERA_PKG::USERREQ")
  (make-package "CAMERA_PKG::USERREQ"))
(unless (find-package "CAMERA_PKG::USERREQREQUEST")
  (make-package "CAMERA_PKG::USERREQREQUEST"))
(unless (find-package "CAMERA_PKG::USERREQRESPONSE")
  (make-package "CAMERA_PKG::USERREQRESPONSE"))

(in-package "ROS")





(defclass camera_pkg::UserReqRequest
  :super ros::object
  :slots ())

(defmethod camera_pkg::UserReqRequest
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

(defclass camera_pkg::UserReqResponse
  :super ros::object
  :slots (_num _stitches ))

(defmethod camera_pkg::UserReqResponse
  (:init
   (&key
    ((:num __num) 0)
    ((:stitches __stitches) (make-array 0 :initial-element 0.0 :element-type :float))
    )
   (send-super :init)
   (setq _num (round __num))
   (setq _stitches __stitches)
   self)
  (:num
   (&optional __num)
   (if __num (setq _num __num)) _num)
  (:stitches
   (&optional __stitches)
   (if __stitches (setq _stitches __stitches)) _stitches)
  (:serialization-length
   ()
   (+
    ;; int64 _num
    8
    ;; float64[] _stitches
    (* 8    (length _stitches)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int64 _num
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _num (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _num) (= (length (_num . bv)) 2)) ;; bignum
              (write-long (ash (elt (_num . bv) 0) 0) s)
              (write-long (ash (elt (_num . bv) 1) -1) s))
             ((and (class _num) (= (length (_num . bv)) 1)) ;; big1
              (write-long (elt (_num . bv) 0) s)
              (write-long (if (>= _num 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _num s)(write-long (if (>= _num 0) 0 #xffffffff) s)))
     ;; float64[] _stitches
     (write-long (length _stitches) s)
     (dotimes (i (length _stitches))
       (sys::poke (elt _stitches i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int64 _num
#+(or :alpha :irix6 :x86_64)
      (setf _num (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _num (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;; float64[] _stitches
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _stitches (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _stitches i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;;
   self)
  )

(defclass camera_pkg::UserReq
  :super ros::object
  :slots ())

(setf (get camera_pkg::UserReq :md5sum-) "728e20175689a0067ab9e0629d227334")
(setf (get camera_pkg::UserReq :datatype-) "camera_pkg/UserReq")
(setf (get camera_pkg::UserReq :request) camera_pkg::UserReqRequest)
(setf (get camera_pkg::UserReq :response) camera_pkg::UserReqResponse)

(defmethod camera_pkg::UserReqRequest
  (:response () (instance camera_pkg::UserReqResponse :init)))

(setf (get camera_pkg::UserReqRequest :md5sum-) "728e20175689a0067ab9e0629d227334")
(setf (get camera_pkg::UserReqRequest :datatype-) "camera_pkg/UserReqRequest")
(setf (get camera_pkg::UserReqRequest :definition-)
      "---
int64 num
float64[] stitches

")

(setf (get camera_pkg::UserReqResponse :md5sum-) "728e20175689a0067ab9e0629d227334")
(setf (get camera_pkg::UserReqResponse :datatype-) "camera_pkg/UserReqResponse")
(setf (get camera_pkg::UserReqResponse :definition-)
      "---
int64 num
float64[] stitches

")



(provide :camera_pkg/UserReq "728e20175689a0067ab9e0629d227334")


