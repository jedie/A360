# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: user_database.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='user_database.proto',
  package='data',
  serialized_pb=_b('\n\x13user_database.proto\x12\x04\x64\x61ta\"&\n\x08PbUserDb\x12\x1a\n\x12\x63urrent_user_index\x18\x01 \x02(\r')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PBUSERDB = _descriptor.Descriptor(
  name='PbUserDb',
  full_name='data.PbUserDb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='current_user_index', full_name='data.PbUserDb.current_user_index', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=29,
  serialized_end=67,
)

DESCRIPTOR.message_types_by_name['PbUserDb'] = _PBUSERDB

PbUserDb = _reflection.GeneratedProtocolMessageType('PbUserDb', (_message.Message,), dict(
  DESCRIPTOR = _PBUSERDB,
  __module__ = 'user_database_pb2'
  # @@protoc_insertion_point(class_scope:data.PbUserDb)
  ))
_sym_db.RegisterMessage(PbUserDb)


# @@protoc_insertion_point(module_scope)