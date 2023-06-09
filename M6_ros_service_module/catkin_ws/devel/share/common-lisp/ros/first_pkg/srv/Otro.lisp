; Auto-generated. Do not edit!


(cl:in-package first_pkg-srv)


;//! \htmlinclude Otro-request.msg.html

(cl:defclass <Otro-request> (roslisp-msg-protocol:ros-message)
  ((a
    :reader a
    :initarg :a
    :type cl:integer
    :initform 0))
)

(cl:defclass Otro-request (<Otro-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Otro-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Otro-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name first_pkg-srv:<Otro-request> is deprecated: use first_pkg-srv:Otro-request instead.")))

(cl:ensure-generic-function 'a-val :lambda-list '(m))
(cl:defmethod a-val ((m <Otro-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader first_pkg-srv:a-val is deprecated.  Use first_pkg-srv:a instead.")
  (a m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Otro-request>) ostream)
  "Serializes a message object of type '<Otro-request>"
  (cl:let* ((signed (cl:slot-value msg 'a)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 18446744073709551616) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Otro-request>) istream)
  "Deserializes a message object of type '<Otro-request>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'a) (cl:if (cl:< unsigned 9223372036854775808) unsigned (cl:- unsigned 18446744073709551616))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Otro-request>)))
  "Returns string type for a service object of type '<Otro-request>"
  "first_pkg/OtroRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Otro-request)))
  "Returns string type for a service object of type 'Otro-request"
  "first_pkg/OtroRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Otro-request>)))
  "Returns md5sum for a message object of type '<Otro-request>"
  "019706110004b728d56d8baaa8e32797")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Otro-request)))
  "Returns md5sum for a message object of type 'Otro-request"
  "019706110004b728d56d8baaa8e32797")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Otro-request>)))
  "Returns full string definition for message of type '<Otro-request>"
  (cl:format cl:nil "int64 a~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Otro-request)))
  "Returns full string definition for message of type 'Otro-request"
  (cl:format cl:nil "int64 a~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Otro-request>))
  (cl:+ 0
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Otro-request>))
  "Converts a ROS message object to a list"
  (cl:list 'Otro-request
    (cl:cons ':a (a msg))
))
;//! \htmlinclude Otro-response.msg.html

(cl:defclass <Otro-response> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass Otro-response (<Otro-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Otro-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Otro-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name first_pkg-srv:<Otro-response> is deprecated: use first_pkg-srv:Otro-response instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Otro-response>) ostream)
  "Serializes a message object of type '<Otro-response>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Otro-response>) istream)
  "Deserializes a message object of type '<Otro-response>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Otro-response>)))
  "Returns string type for a service object of type '<Otro-response>"
  "first_pkg/OtroResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Otro-response)))
  "Returns string type for a service object of type 'Otro-response"
  "first_pkg/OtroResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Otro-response>)))
  "Returns md5sum for a message object of type '<Otro-response>"
  "019706110004b728d56d8baaa8e32797")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Otro-response)))
  "Returns md5sum for a message object of type 'Otro-response"
  "019706110004b728d56d8baaa8e32797")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Otro-response>)))
  "Returns full string definition for message of type '<Otro-response>"
  (cl:format cl:nil "~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Otro-response)))
  "Returns full string definition for message of type 'Otro-response"
  (cl:format cl:nil "~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Otro-response>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Otro-response>))
  "Converts a ROS message object to a list"
  (cl:list 'Otro-response
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'Otro)))
  'Otro-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'Otro)))
  'Otro-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Otro)))
  "Returns string type for a service object of type '<Otro>"
  "first_pkg/Otro")