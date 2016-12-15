# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: planned_route.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import structures_pb2
import types_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='planned_route.proto',
  package='data',
  serialized_pb=_b('\n\x13planned_route.proto\x12\x04\x64\x61ta\x1a\x10structures.proto\x1a\x0btypes.proto\"Y\n\x0cPbRoutePoint\x12\x10\n\x08x_offset\x18\x01 \x02(\x11\x12\x10\n\x08y_offset\x18\x02 \x02(\x11\x12\x13\n\x0btime_offset\x18\x03 \x01(\r\x12\x10\n\x08z_offset\x18\x04 \x01(\x11\"\xbc\x01\n\x0ePbPlannedRoute\x12\x1c\n\x08route_id\x18\x01 \x02(\x0b\x32\n.PbRouteId\x12\x1c\n\x04name\x18\x02 \x02(\x0b\x32\x0e.PbOneLineText\x12\x0e\n\x06length\x18\x03 \x01(\x02\x12#\n\x0estart_location\x18\x04 \x01(\x0b\x32\x0b.PbLocation\x12\x16\n\x0estart_altitude\x18\x05 \x01(\x02\x12!\n\x05point\x18\x06 \x03(\x0b\x32\x12.data.PbRoutePoint')
  ,
  dependencies=[structures_pb2.DESCRIPTOR,types_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PBROUTEPOINT = _descriptor.Descriptor(
  name='PbRoutePoint',
  full_name='data.PbRoutePoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x_offset', full_name='data.PbRoutePoint.x_offset', index=0,
      number=1, type=17, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y_offset', full_name='data.PbRoutePoint.y_offset', index=1,
      number=2, type=17, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='time_offset', full_name='data.PbRoutePoint.time_offset', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='z_offset', full_name='data.PbRoutePoint.z_offset', index=3,
      number=4, type=17, cpp_type=1, label=1,
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
  serialized_start=60,
  serialized_end=149,
)


_PBPLANNEDROUTE = _descriptor.Descriptor(
  name='PbPlannedRoute',
  full_name='data.PbPlannedRoute',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='route_id', full_name='data.PbPlannedRoute.route_id', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='data.PbPlannedRoute.name', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='length', full_name='data.PbPlannedRoute.length', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start_location', full_name='data.PbPlannedRoute.start_location', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start_altitude', full_name='data.PbPlannedRoute.start_altitude', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='point', full_name='data.PbPlannedRoute.point', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=152,
  serialized_end=340,
)

_PBPLANNEDROUTE.fields_by_name['route_id'].message_type = structures_pb2._PBROUTEID
_PBPLANNEDROUTE.fields_by_name['name'].message_type = structures_pb2._PBONELINETEXT
_PBPLANNEDROUTE.fields_by_name['start_location'].message_type = types_pb2._PBLOCATION
_PBPLANNEDROUTE.fields_by_name['point'].message_type = _PBROUTEPOINT
DESCRIPTOR.message_types_by_name['PbRoutePoint'] = _PBROUTEPOINT
DESCRIPTOR.message_types_by_name['PbPlannedRoute'] = _PBPLANNEDROUTE

PbRoutePoint = _reflection.GeneratedProtocolMessageType('PbRoutePoint', (_message.Message,), dict(
  DESCRIPTOR = _PBROUTEPOINT,
  __module__ = 'planned_route_pb2'
  # @@protoc_insertion_point(class_scope:data.PbRoutePoint)
  ))
_sym_db.RegisterMessage(PbRoutePoint)

PbPlannedRoute = _reflection.GeneratedProtocolMessageType('PbPlannedRoute', (_message.Message,), dict(
  DESCRIPTOR = _PBPLANNEDROUTE,
  __module__ = 'planned_route_pb2'
  # @@protoc_insertion_point(class_scope:data.PbPlannedRoute)
  ))
_sym_db.RegisterMessage(PbPlannedRoute)


# @@protoc_insertion_point(module_scope)
