# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from safe_landing_planner/SLPGridMsg.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import std_msgs.msg

class SLPGridMsg(genpy.Message):
  _md5sum = "ac7dcafe4e3af4e98f04adc7a210b7be"
  _type = "safe_landing_planner/SLPGridMsg"
  _has_header = True  # flag to mark the presence of a Header object
  _full_text = """Header header
std_msgs/Float64MultiArray mean
std_msgs/Float64MultiArray std_dev
std_msgs/Int64MultiArray counter
std_msgs/Int64MultiArray land

float64 grid_size
float64 cell_size

geometry_msgs/Vector3 curr_pos_index

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

================================================================================
MSG: std_msgs/Float64MultiArray
# Please look at the MultiArrayLayout message definition for
# documentation on all multiarrays.

MultiArrayLayout  layout        # specification of data layout
float64[]         data          # array of data


================================================================================
MSG: std_msgs/MultiArrayLayout
# The multiarray declares a generic multi-dimensional array of a
# particular data type.  Dimensions are ordered from outer most
# to inner most.

MultiArrayDimension[] dim # Array of dimension properties
uint32 data_offset        # padding elements at front of data

# Accessors should ALWAYS be written in terms of dimension stride
# and specified outer-most dimension first.
# 
# multiarray(i,j,k) = data[data_offset + dim_stride[1]*i + dim_stride[2]*j + k]
#
# A standard, 3-channel 640x480 image with interleaved color channels
# would be specified as:
#
# dim[0].label  = "height"
# dim[0].size   = 480
# dim[0].stride = 3*640*480 = 921600  (note dim[0] stride is just size of image)
# dim[1].label  = "width"
# dim[1].size   = 640
# dim[1].stride = 3*640 = 1920
# dim[2].label  = "channel"
# dim[2].size   = 3
# dim[2].stride = 3
#
# multiarray(i,j,k) refers to the ith row, jth column, and kth channel.

================================================================================
MSG: std_msgs/MultiArrayDimension
string label   # label of given dimension
uint32 size    # size of given dimension (in type units)
uint32 stride  # stride of given dimension
================================================================================
MSG: std_msgs/Int64MultiArray
# Please look at the MultiArrayLayout message definition for
# documentation on all multiarrays.

MultiArrayLayout  layout        # specification of data layout
int64[]           data          # array of data


================================================================================
MSG: geometry_msgs/Vector3
# This represents a vector in free space. 
# It is only meant to represent a direction. Therefore, it does not
# make sense to apply a translation to it (e.g., when applying a 
# generic rigid transformation to a Vector3, tf2 will only apply the
# rotation). If you want your data to be translatable too, use the
# geometry_msgs/Point message instead.

float64 x
float64 y
float64 z"""
  __slots__ = ['header','mean','std_dev','counter','land','grid_size','cell_size','curr_pos_index']
  _slot_types = ['std_msgs/Header','std_msgs/Float64MultiArray','std_msgs/Float64MultiArray','std_msgs/Int64MultiArray','std_msgs/Int64MultiArray','float64','float64','geometry_msgs/Vector3']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,mean,std_dev,counter,land,grid_size,cell_size,curr_pos_index

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(SLPGridMsg, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.mean is None:
        self.mean = std_msgs.msg.Float64MultiArray()
      if self.std_dev is None:
        self.std_dev = std_msgs.msg.Float64MultiArray()
      if self.counter is None:
        self.counter = std_msgs.msg.Int64MultiArray()
      if self.land is None:
        self.land = std_msgs.msg.Int64MultiArray()
      if self.grid_size is None:
        self.grid_size = 0.
      if self.cell_size is None:
        self.cell_size = 0.
      if self.curr_pos_index is None:
        self.curr_pos_index = geometry_msgs.msg.Vector3()
    else:
      self.header = std_msgs.msg.Header()
      self.mean = std_msgs.msg.Float64MultiArray()
      self.std_dev = std_msgs.msg.Float64MultiArray()
      self.counter = std_msgs.msg.Int64MultiArray()
      self.land = std_msgs.msg.Int64MultiArray()
      self.grid_size = 0.
      self.cell_size = 0.
      self.curr_pos_index = geometry_msgs.msg.Vector3()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      length = len(self.mean.layout.dim)
      buff.write(_struct_I.pack(length))
      for val1 in self.mean.layout.dim:
        _x = val1.label
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _x = val1
        buff.write(_get_struct_2I().pack(_x.size, _x.stride))
      _x = self.mean.layout.data_offset
      buff.write(_get_struct_I().pack(_x))
      length = len(self.mean.data)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.mean.data))
      length = len(self.std_dev.layout.dim)
      buff.write(_struct_I.pack(length))
      for val1 in self.std_dev.layout.dim:
        _x = val1.label
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _x = val1
        buff.write(_get_struct_2I().pack(_x.size, _x.stride))
      _x = self.std_dev.layout.data_offset
      buff.write(_get_struct_I().pack(_x))
      length = len(self.std_dev.data)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(struct.Struct(pattern).pack(*self.std_dev.data))
      length = len(self.counter.layout.dim)
      buff.write(_struct_I.pack(length))
      for val1 in self.counter.layout.dim:
        _x = val1.label
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _x = val1
        buff.write(_get_struct_2I().pack(_x.size, _x.stride))
      _x = self.counter.layout.data_offset
      buff.write(_get_struct_I().pack(_x))
      length = len(self.counter.data)
      buff.write(_struct_I.pack(length))
      pattern = '<%sq'%length
      buff.write(struct.Struct(pattern).pack(*self.counter.data))
      length = len(self.land.layout.dim)
      buff.write(_struct_I.pack(length))
      for val1 in self.land.layout.dim:
        _x = val1.label
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _x = val1
        buff.write(_get_struct_2I().pack(_x.size, _x.stride))
      _x = self.land.layout.data_offset
      buff.write(_get_struct_I().pack(_x))
      length = len(self.land.data)
      buff.write(_struct_I.pack(length))
      pattern = '<%sq'%length
      buff.write(struct.Struct(pattern).pack(*self.land.data))
      _x = self
      buff.write(_get_struct_5d().pack(_x.grid_size, _x.cell_size, _x.curr_pos_index.x, _x.curr_pos_index.y, _x.curr_pos_index.z))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.mean is None:
        self.mean = std_msgs.msg.Float64MultiArray()
      if self.std_dev is None:
        self.std_dev = std_msgs.msg.Float64MultiArray()
      if self.counter is None:
        self.counter = std_msgs.msg.Int64MultiArray()
      if self.land is None:
        self.land = std_msgs.msg.Int64MultiArray()
      if self.curr_pos_index is None:
        self.curr_pos_index = geometry_msgs.msg.Vector3()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.mean.layout.dim = []
      for i in range(0, length):
        val1 = std_msgs.msg.MultiArrayDimension()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.label = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.label = str[start:end]
        _x = val1
        start = end
        end += 8
        (_x.size, _x.stride,) = _get_struct_2I().unpack(str[start:end])
        self.mean.layout.dim.append(val1)
      start = end
      end += 4
      (self.mean.layout.data_offset,) = _get_struct_I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.mean.data = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.std_dev.layout.dim = []
      for i in range(0, length):
        val1 = std_msgs.msg.MultiArrayDimension()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.label = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.label = str[start:end]
        _x = val1
        start = end
        end += 8
        (_x.size, _x.stride,) = _get_struct_2I().unpack(str[start:end])
        self.std_dev.layout.dim.append(val1)
      start = end
      end += 4
      (self.std_dev.layout.data_offset,) = _get_struct_I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.std_dev.data = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.counter.layout.dim = []
      for i in range(0, length):
        val1 = std_msgs.msg.MultiArrayDimension()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.label = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.label = str[start:end]
        _x = val1
        start = end
        end += 8
        (_x.size, _x.stride,) = _get_struct_2I().unpack(str[start:end])
        self.counter.layout.dim.append(val1)
      start = end
      end += 4
      (self.counter.layout.data_offset,) = _get_struct_I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sq'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.counter.data = s.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.land.layout.dim = []
      for i in range(0, length):
        val1 = std_msgs.msg.MultiArrayDimension()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.label = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.label = str[start:end]
        _x = val1
        start = end
        end += 8
        (_x.size, _x.stride,) = _get_struct_2I().unpack(str[start:end])
        self.land.layout.dim.append(val1)
      start = end
      end += 4
      (self.land.layout.data_offset,) = _get_struct_I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sq'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.land.data = s.unpack(str[start:end])
      _x = self
      start = end
      end += 40
      (_x.grid_size, _x.cell_size, _x.curr_pos_index.x, _x.curr_pos_index.y, _x.curr_pos_index.z,) = _get_struct_5d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      length = len(self.mean.layout.dim)
      buff.write(_struct_I.pack(length))
      for val1 in self.mean.layout.dim:
        _x = val1.label
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _x = val1
        buff.write(_get_struct_2I().pack(_x.size, _x.stride))
      _x = self.mean.layout.data_offset
      buff.write(_get_struct_I().pack(_x))
      length = len(self.mean.data)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.mean.data.tostring())
      length = len(self.std_dev.layout.dim)
      buff.write(_struct_I.pack(length))
      for val1 in self.std_dev.layout.dim:
        _x = val1.label
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _x = val1
        buff.write(_get_struct_2I().pack(_x.size, _x.stride))
      _x = self.std_dev.layout.data_offset
      buff.write(_get_struct_I().pack(_x))
      length = len(self.std_dev.data)
      buff.write(_struct_I.pack(length))
      pattern = '<%sd'%length
      buff.write(self.std_dev.data.tostring())
      length = len(self.counter.layout.dim)
      buff.write(_struct_I.pack(length))
      for val1 in self.counter.layout.dim:
        _x = val1.label
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _x = val1
        buff.write(_get_struct_2I().pack(_x.size, _x.stride))
      _x = self.counter.layout.data_offset
      buff.write(_get_struct_I().pack(_x))
      length = len(self.counter.data)
      buff.write(_struct_I.pack(length))
      pattern = '<%sq'%length
      buff.write(self.counter.data.tostring())
      length = len(self.land.layout.dim)
      buff.write(_struct_I.pack(length))
      for val1 in self.land.layout.dim:
        _x = val1.label
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _x = val1
        buff.write(_get_struct_2I().pack(_x.size, _x.stride))
      _x = self.land.layout.data_offset
      buff.write(_get_struct_I().pack(_x))
      length = len(self.land.data)
      buff.write(_struct_I.pack(length))
      pattern = '<%sq'%length
      buff.write(self.land.data.tostring())
      _x = self
      buff.write(_get_struct_5d().pack(_x.grid_size, _x.cell_size, _x.curr_pos_index.x, _x.curr_pos_index.y, _x.curr_pos_index.z))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.mean is None:
        self.mean = std_msgs.msg.Float64MultiArray()
      if self.std_dev is None:
        self.std_dev = std_msgs.msg.Float64MultiArray()
      if self.counter is None:
        self.counter = std_msgs.msg.Int64MultiArray()
      if self.land is None:
        self.land = std_msgs.msg.Int64MultiArray()
      if self.curr_pos_index is None:
        self.curr_pos_index = geometry_msgs.msg.Vector3()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.mean.layout.dim = []
      for i in range(0, length):
        val1 = std_msgs.msg.MultiArrayDimension()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.label = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.label = str[start:end]
        _x = val1
        start = end
        end += 8
        (_x.size, _x.stride,) = _get_struct_2I().unpack(str[start:end])
        self.mean.layout.dim.append(val1)
      start = end
      end += 4
      (self.mean.layout.data_offset,) = _get_struct_I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.mean.data = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.std_dev.layout.dim = []
      for i in range(0, length):
        val1 = std_msgs.msg.MultiArrayDimension()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.label = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.label = str[start:end]
        _x = val1
        start = end
        end += 8
        (_x.size, _x.stride,) = _get_struct_2I().unpack(str[start:end])
        self.std_dev.layout.dim.append(val1)
      start = end
      end += 4
      (self.std_dev.layout.data_offset,) = _get_struct_I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sd'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.std_dev.data = numpy.frombuffer(str[start:end], dtype=numpy.float64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.counter.layout.dim = []
      for i in range(0, length):
        val1 = std_msgs.msg.MultiArrayDimension()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.label = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.label = str[start:end]
        _x = val1
        start = end
        end += 8
        (_x.size, _x.stride,) = _get_struct_2I().unpack(str[start:end])
        self.counter.layout.dim.append(val1)
      start = end
      end += 4
      (self.counter.layout.data_offset,) = _get_struct_I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sq'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.counter.data = numpy.frombuffer(str[start:end], dtype=numpy.int64, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.land.layout.dim = []
      for i in range(0, length):
        val1 = std_msgs.msg.MultiArrayDimension()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1.label = str[start:end].decode('utf-8', 'rosmsg')
        else:
          val1.label = str[start:end]
        _x = val1
        start = end
        end += 8
        (_x.size, _x.stride,) = _get_struct_2I().unpack(str[start:end])
        self.land.layout.dim.append(val1)
      start = end
      end += 4
      (self.land.layout.data_offset,) = _get_struct_I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sq'%length
      start = end
      s = struct.Struct(pattern)
      end += s.size
      self.land.data = numpy.frombuffer(str[start:end], dtype=numpy.int64, count=length)
      _x = self
      start = end
      end += 40
      (_x.grid_size, _x.cell_size, _x.curr_pos_index.x, _x.curr_pos_index.y, _x.curr_pos_index.z,) = _get_struct_5d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2I = None
def _get_struct_2I():
    global _struct_2I
    if _struct_2I is None:
        _struct_2I = struct.Struct("<2I")
    return _struct_2I
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_5d = None
def _get_struct_5d():
    global _struct_5d
    if _struct_5d is None:
        _struct_5d = struct.Struct("<5d")
    return _struct_5d