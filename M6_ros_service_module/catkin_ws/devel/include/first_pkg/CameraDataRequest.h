// Generated by gencpp from file first_pkg/CameraDataRequest.msg
// DO NOT EDIT!


#ifndef FIRST_PKG_MESSAGE_CAMERADATAREQUEST_H
#define FIRST_PKG_MESSAGE_CAMERADATAREQUEST_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace first_pkg
{
template <class ContainerAllocator>
struct CameraDataRequest_
{
  typedef CameraDataRequest_<ContainerAllocator> Type;

  CameraDataRequest_()
    : a(0)
    , b(0)  {
    }
  CameraDataRequest_(const ContainerAllocator& _alloc)
    : a(0)
    , b(0)  {
  (void)_alloc;
    }



   typedef int64_t _a_type;
  _a_type a;

   typedef int64_t _b_type;
  _b_type b;





  typedef boost::shared_ptr< ::first_pkg::CameraDataRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::first_pkg::CameraDataRequest_<ContainerAllocator> const> ConstPtr;

}; // struct CameraDataRequest_

typedef ::first_pkg::CameraDataRequest_<std::allocator<void> > CameraDataRequest;

typedef boost::shared_ptr< ::first_pkg::CameraDataRequest > CameraDataRequestPtr;
typedef boost::shared_ptr< ::first_pkg::CameraDataRequest const> CameraDataRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::first_pkg::CameraDataRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::first_pkg::CameraDataRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::first_pkg::CameraDataRequest_<ContainerAllocator1> & lhs, const ::first_pkg::CameraDataRequest_<ContainerAllocator2> & rhs)
{
  return lhs.a == rhs.a &&
    lhs.b == rhs.b;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::first_pkg::CameraDataRequest_<ContainerAllocator1> & lhs, const ::first_pkg::CameraDataRequest_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace first_pkg

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::first_pkg::CameraDataRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::first_pkg::CameraDataRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::first_pkg::CameraDataRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::first_pkg::CameraDataRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::first_pkg::CameraDataRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::first_pkg::CameraDataRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::first_pkg::CameraDataRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "36d09b846be0b371c5f190354dd3153e";
  }

  static const char* value(const ::first_pkg::CameraDataRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x36d09b846be0b371ULL;
  static const uint64_t static_value2 = 0xc5f190354dd3153eULL;
};

template<class ContainerAllocator>
struct DataType< ::first_pkg::CameraDataRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "first_pkg/CameraDataRequest";
  }

  static const char* value(const ::first_pkg::CameraDataRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::first_pkg::CameraDataRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "int64 a\n"
"int64 b\n"
;
  }

  static const char* value(const ::first_pkg::CameraDataRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::first_pkg::CameraDataRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.a);
      stream.next(m.b);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct CameraDataRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::first_pkg::CameraDataRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::first_pkg::CameraDataRequest_<ContainerAllocator>& v)
  {
    s << indent << "a: ";
    Printer<int64_t>::stream(s, indent + "  ", v.a);
    s << indent << "b: ";
    Printer<int64_t>::stream(s, indent + "  ", v.b);
  }
};

} // namespace message_operations
} // namespace ros

#endif // FIRST_PKG_MESSAGE_CAMERADATAREQUEST_H
