; Auto-generated. Do not edit!


(cl:in-package camera_pkg-srv)


;//! \htmlinclude CameraData-request.msg.html

(cl:defclass <CameraData-request> (roslisp-msg-protocol:ros-message)
  ((num
    :reader num
    :initarg :num
    :type cl:integer
    :initform 0)
   (stitches
    :reader stitches
    :initarg :stitches
    :type (cl:vector cl:float)
   :initform (cl:make-array 0 :element-type 'cl:float :initial-element 0.0)))
)

(cl:defclass CameraData-request (<CameraData-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <CameraData-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'CameraData-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name camera_pkg-srv:<CameraData-request> is deprecated: use camera_pkg-srv:CameraData-request instead.")))

(cl:ensure-generic-function 'num-val :lambda-list '(m))
(cl:defmethod num-val ((m <CameraData-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader camera_pkg-srv:num-val is deprecated.  Use camera_pkg-srv:num instead.")
  (num m))

(cl:ensure-generic-function 'stitches-val :lambda-list '(m))
(cl:defmethod stitches-val ((m <CameraData-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader camera_pkg-srv:stitches-val is deprecated.  Use camera_pkg-srv:stitches instead.")
  (stitches m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <CameraData-request>) ostream)
  "Serializes a message object of type '<CameraData-request>"
  (cl:let* ((signed (cl:slot-value msg 'num)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 18446744073709551616) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) unsigned) ostream)
    )
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'stitches))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-double-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream)))
   (cl:slot-value msg 'stitches))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <CameraData-request>) istream)
  "Deserializes a message object of type '<CameraData-request>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'num) (cl:if (cl:< unsigned 9223372036854775808) unsigned (cl:- unsigned 18446744073709551616))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'stitches) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'stitches)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-double-float-bits bits))))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<CameraData-request>)))
  "Returns string type for a service object of type '<CameraData-request>"
  "camera_pkg/CameraDataRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'CameraData-request)))
  "Returns string type for a service object of type 'CameraData-request"
  "camera_pkg/CameraDataRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<CameraData-request>)))
  "Returns md5sum for a message object of type '<CameraData-request>"
  "728e20175689a0067ab9e0629d227334")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'CameraData-request)))
  "Returns md5sum for a message object of type 'CameraData-request"
  "728e20175689a0067ab9e0629d227334")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<CameraData-request>)))
  "Returns full string definition for message of type '<CameraData-request>"
  (cl:format cl:nil "int64 num~%float64[] stitches~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'CameraData-request)))
  "Returns full string definition for message of type 'CameraData-request"
  (cl:format cl:nil "int64 num~%float64[] stitches~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <CameraData-request>))
  (cl:+ 0
     8
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'stitches) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 8)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <CameraData-request>))
  "Converts a ROS message object to a list"
  (cl:list 'CameraData-request
    (cl:cons ':num (num msg))
    (cl:cons ':stitches (stitches msg))
))
;//! \htmlinclude CameraData-response.msg.html

(cl:defclass <CameraData-response> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass CameraData-response (<CameraData-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <CameraData-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'CameraData-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name camera_pkg-srv:<CameraData-response> is deprecated: use camera_pkg-srv:CameraData-response instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <CameraData-response>) ostream)
  "Serializes a message object of type '<CameraData-response>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <CameraData-response>) istream)
  "Deserializes a message object of type '<CameraData-response>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<CameraData-response>)))
  "Returns string type for a service object of type '<CameraData-response>"
  "camera_pkg/CameraDataResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'CameraData-response)))
  "Returns string type for a service object of type 'CameraData-response"
  "camera_pkg/CameraDataResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<CameraData-response>)))
  "Returns md5sum for a message object of type '<CameraData-response>"
  "728e20175689a0067ab9e0629d227334")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'CameraData-response)))
  "Returns md5sum for a message object of type 'CameraData-response"
  "728e20175689a0067ab9e0629d227334")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<CameraData-response>)))
  "Returns full string definition for message of type '<CameraData-response>"
  (cl:format cl:nil "~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'CameraData-response)))
  "Returns full string definition for message of type 'CameraData-response"
  (cl:format cl:nil "~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <CameraData-response>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <CameraData-response>))
  "Converts a ROS message object to a list"
  (cl:list 'CameraData-response
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'CameraData)))
  'CameraData-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'CameraData)))
  'CameraData-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'CameraData)))
  "Returns string type for a service object of type '<CameraData>"
  "camera_pkg/CameraData")