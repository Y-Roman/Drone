# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from ros_vosk/speech_recognition.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import genpy

class speech_recognition(genpy.Message):
  _md5sum = "d3b0b667a7ab9370dea4b81b6e8de6c9"
  _type = "ros_vosk/speech_recognition"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """time    time_recognized
string  final_result
string  partial_result 
bool    isSpeech_recognized"""
  __slots__ = ['time_recognized','final_result','partial_result','isSpeech_recognized']
  _slot_types = ['time','string','string','bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       time_recognized,final_result,partial_result,isSpeech_recognized

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(speech_recognition, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.time_recognized is None:
        self.time_recognized = genpy.Time()
      if self.final_result is None:
        self.final_result = ''
      if self.partial_result is None:
        self.partial_result = ''
      if self.isSpeech_recognized is None:
        self.isSpeech_recognized = False
    else:
      self.time_recognized = genpy.Time()
      self.final_result = ''
      self.partial_result = ''
      self.isSpeech_recognized = False

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
      buff.write(_get_struct_2I().pack(_x.time_recognized.secs, _x.time_recognized.nsecs))
      _x = self.final_result
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.partial_result
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.isSpeech_recognized
      buff.write(_get_struct_B().pack(_x))
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
      if self.time_recognized is None:
        self.time_recognized = genpy.Time()
      end = 0
      _x = self
      start = end
      end += 8
      (_x.time_recognized.secs, _x.time_recognized.nsecs,) = _get_struct_2I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.final_result = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.final_result = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.partial_result = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.partial_result = str[start:end]
      start = end
      end += 1
      (self.isSpeech_recognized,) = _get_struct_B().unpack(str[start:end])
      self.isSpeech_recognized = bool(self.isSpeech_recognized)
      self.time_recognized.canon()
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
      buff.write(_get_struct_2I().pack(_x.time_recognized.secs, _x.time_recognized.nsecs))
      _x = self.final_result
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.partial_result
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.isSpeech_recognized
      buff.write(_get_struct_B().pack(_x))
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
      if self.time_recognized is None:
        self.time_recognized = genpy.Time()
      end = 0
      _x = self
      start = end
      end += 8
      (_x.time_recognized.secs, _x.time_recognized.nsecs,) = _get_struct_2I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.final_result = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.final_result = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.partial_result = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.partial_result = str[start:end]
      start = end
      end += 1
      (self.isSpeech_recognized,) = _get_struct_B().unpack(str[start:end])
      self.isSpeech_recognized = bool(self.isSpeech_recognized)
      self.time_recognized.canon()
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
_struct_B = None
def _get_struct_B():
    global _struct_B
    if _struct_B is None:
        _struct_B = struct.Struct("<B")
    return _struct_B
