// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from multisense_msgs:msg/StampedPps.idl
// generated code does not contain a copyright notice

#ifndef MULTISENSE_MSGS__MSG__DETAIL__STAMPED_PPS__TRAITS_HPP_
#define MULTISENSE_MSGS__MSG__DETAIL__STAMPED_PPS__TRAITS_HPP_

#include "multisense_msgs/msg/detail/stamped_pps__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

// Include directives for member types
// Member 'data'
// Member 'host_time'
#include "builtin_interfaces/msg/detail/time__traits.hpp"

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<multisense_msgs::msg::StampedPps>()
{
  return "multisense_msgs::msg::StampedPps";
}

template<>
inline const char * name<multisense_msgs::msg::StampedPps>()
{
  return "multisense_msgs/msg/StampedPps";
}

template<>
struct has_fixed_size<multisense_msgs::msg::StampedPps>
  : std::integral_constant<bool, has_fixed_size<builtin_interfaces::msg::Time>::value> {};

template<>
struct has_bounded_size<multisense_msgs::msg::StampedPps>
  : std::integral_constant<bool, has_bounded_size<builtin_interfaces::msg::Time>::value> {};

template<>
struct is_message<multisense_msgs::msg::StampedPps>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // MULTISENSE_MSGS__MSG__DETAIL__STAMPED_PPS__TRAITS_HPP_
