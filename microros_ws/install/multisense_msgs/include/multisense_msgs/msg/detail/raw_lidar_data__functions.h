// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from multisense_msgs:msg/RawLidarData.idl
// generated code does not contain a copyright notice

#ifndef MULTISENSE_MSGS__MSG__DETAIL__RAW_LIDAR_DATA__FUNCTIONS_H_
#define MULTISENSE_MSGS__MSG__DETAIL__RAW_LIDAR_DATA__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "multisense_msgs/msg/rosidl_generator_c__visibility_control.h"

#include "multisense_msgs/msg/detail/raw_lidar_data__struct.h"

/// Initialize msg/RawLidarData message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * multisense_msgs__msg__RawLidarData
 * )) before or use
 * multisense_msgs__msg__RawLidarData__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_multisense_msgs
bool
multisense_msgs__msg__RawLidarData__init(multisense_msgs__msg__RawLidarData * msg);

/// Finalize msg/RawLidarData message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_multisense_msgs
void
multisense_msgs__msg__RawLidarData__fini(multisense_msgs__msg__RawLidarData * msg);

/// Create msg/RawLidarData message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * multisense_msgs__msg__RawLidarData__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_multisense_msgs
multisense_msgs__msg__RawLidarData *
multisense_msgs__msg__RawLidarData__create();

/// Destroy msg/RawLidarData message.
/**
 * It calls
 * multisense_msgs__msg__RawLidarData__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_multisense_msgs
void
multisense_msgs__msg__RawLidarData__destroy(multisense_msgs__msg__RawLidarData * msg);

/// Check for msg/RawLidarData message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_multisense_msgs
bool
multisense_msgs__msg__RawLidarData__are_equal(const multisense_msgs__msg__RawLidarData * lhs, const multisense_msgs__msg__RawLidarData * rhs);

/// Copy a msg/RawLidarData message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_multisense_msgs
bool
multisense_msgs__msg__RawLidarData__copy(
  const multisense_msgs__msg__RawLidarData * input,
  multisense_msgs__msg__RawLidarData * output);

/// Initialize array of msg/RawLidarData messages.
/**
 * It allocates the memory for the number of elements and calls
 * multisense_msgs__msg__RawLidarData__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_multisense_msgs
bool
multisense_msgs__msg__RawLidarData__Sequence__init(multisense_msgs__msg__RawLidarData__Sequence * array, size_t size);

/// Finalize array of msg/RawLidarData messages.
/**
 * It calls
 * multisense_msgs__msg__RawLidarData__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_multisense_msgs
void
multisense_msgs__msg__RawLidarData__Sequence__fini(multisense_msgs__msg__RawLidarData__Sequence * array);

/// Create array of msg/RawLidarData messages.
/**
 * It allocates the memory for the array and calls
 * multisense_msgs__msg__RawLidarData__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_multisense_msgs
multisense_msgs__msg__RawLidarData__Sequence *
multisense_msgs__msg__RawLidarData__Sequence__create(size_t size);

/// Destroy array of msg/RawLidarData messages.
/**
 * It calls
 * multisense_msgs__msg__RawLidarData__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_multisense_msgs
void
multisense_msgs__msg__RawLidarData__Sequence__destroy(multisense_msgs__msg__RawLidarData__Sequence * array);

/// Check for msg/RawLidarData message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_multisense_msgs
bool
multisense_msgs__msg__RawLidarData__Sequence__are_equal(const multisense_msgs__msg__RawLidarData__Sequence * lhs, const multisense_msgs__msg__RawLidarData__Sequence * rhs);

/// Copy an array of msg/RawLidarData messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_multisense_msgs
bool
multisense_msgs__msg__RawLidarData__Sequence__copy(
  const multisense_msgs__msg__RawLidarData__Sequence * input,
  multisense_msgs__msg__RawLidarData__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // MULTISENSE_MSGS__MSG__DETAIL__RAW_LIDAR_DATA__FUNCTIONS_H_
