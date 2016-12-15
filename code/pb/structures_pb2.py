# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: structures.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import types_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='structures.proto',
  package='',
  serialized_pb=_b('\n\x10structures.proto\x1a\x0btypes.proto\"\x85\x02\n\x0ePbVolumeTarget\x12\x37\n\x0btarget_type\x18\x01 \x02(\x0e\x32\".PbVolumeTarget.PbVolymeTargetType\x12\x1d\n\x08\x64uration\x18\x02 \x01(\x0b\x32\x0b.PbDuration\x12\x10\n\x08\x64istance\x18\x03 \x01(\x02\x12\x10\n\x08\x63\x61lories\x18\x04 \x01(\r\"w\n\x12PbVolymeTargetType\x12\x1f\n\x1bVOLUME_TARGET_TYPE_DURATION\x10\x00\x12\x1f\n\x1bVOLUME_TARGET_TYPE_DISTANCE\x10\x01\x12\x1f\n\x1bVOLUME_TARGET_TYPE_CALORIES\x10\x02\"\xa7\x01\n\x0ePbTrainingLoad\x12\x19\n\x11training_load_val\x18\x01 \x01(\r\x12\"\n\rrecovery_time\x18\x02 \x01(\x0b\x32\x0b.PbDuration\x12 \n\x18\x63\x61rbohydrate_consumption\x18\x03 \x01(\r\x12\x1b\n\x13protein_consumption\x18\x04 \x01(\r\x12\x17\n\x0f\x66\x61t_consumption\x18\x05 \x01(\r\"<\n\x0fPbHeartRateZone\x12\x13\n\x0blower_limit\x18\x01 \x02(\r\x12\x14\n\x0chigher_limit\x18\x02 \x02(\r\"8\n\x0bPbSpeedZone\x12\x13\n\x0blower_limit\x18\x01 \x02(\x02\x12\x14\n\x0chigher_limit\x18\x02 \x02(\x02\"8\n\x0bPbPowerZone\x12\x13\n\x0blower_limit\x18\x01 \x02(\r\x12\x14\n\x0chigher_limit\x18\x02 \x02(\r\"\xac\x02\n\x07PbZones\x12)\n\x0fheart_rate_zone\x18\x01 \x03(\x0b\x32\x10.PbHeartRateZone\x12 \n\nspeed_zone\x18\x02 \x03(\x0b\x32\x0c.PbSpeedZone\x12 \n\npower_zone\x18\x03 \x03(\x0b\x32\x0c.PbPowerZone\x12@\n\x19heart_rate_setting_source\x18\n \x01(\x0e\x32\x1d.PbHeartRateZoneSettingSource\x12\x37\n\x14power_setting_source\x18\x0b \x01(\x0e\x32\x19.PbPowerZoneSettingSource\x12\x37\n\x14speed_setting_source\x18\x0c \x01(\x0e\x32\x19.PbSpeedZoneSettingSource\"1\n\x08PbBleMac\x12\x0b\n\x03mac\x18\x01 \x02(\x0c\x12\x18\n\x04type\x18\x02 \x02(\x0e\x32\n.PbMacType\"\x1f\n\x0fPbBleDeviceName\x12\x0c\n\x04name\x18\x01 \x02(\t\"\x1f\n\nPbDeviceId\x12\x11\n\tdevice_id\x18\x01 \x02(\t\"F\n\x0ePbRunningIndex\x12\r\n\x05value\x18\x01 \x02(\r\x12%\n\x10\x63\x61lculation_time\x18\x02 \x01(\x0b\x32\x0b.PbDuration\"\"\n\x11PbSportIdentifier\x12\r\n\x05value\x18\x01 \x02(\x04\"\x1d\n\rPbOneLineText\x12\x0c\n\x04text\x18\x01 \x02(\t\"\x1f\n\x0fPbMultiLineText\x12\x0c\n\x04text\x18\x01 \x02(\t\" \n\x0cPbLanguageId\x12\x10\n\x08language\x18\x01 \x02(\t\"T\n\x19PbTrainingSessionTargetId\x12\r\n\x05value\x18\x01 \x02(\x04\x12(\n\rlast_modified\x18\x02 \x01(\x0b\x32\x11.PbSystemDateTime\"V\n\x1bPbTrainingSessionFavoriteId\x12\r\n\x05value\x18\x01 \x02(\x04\x12(\n\rlast_modified\x18\x02 \x01(\x0b\x32\x11.PbSystemDateTime\"\x1a\n\tPbRouteId\x12\r\n\x05value\x18\x01 \x02(\x04\"[\n\x12PbSwimmingPoolInfo\x12\x13\n\x0bpool_length\x18\x01 \x01(\x02\x12\x30\n\x12swimming_pool_type\x18\x02 \x02(\x0e\x32\x14.PbSwimmingPoolUnits\"$\n\x13PbTrainingProgramId\x12\r\n\x05value\x18\x01 \x02(\x04\"\x1a\n\tPbEventId\x12\r\n\x05value\x18\x01 \x02(\x04')
  ,
  dependencies=[types_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_PBVOLUMETARGET_PBVOLYMETARGETTYPE = _descriptor.EnumDescriptor(
  name='PbVolymeTargetType',
  full_name='PbVolumeTarget.PbVolymeTargetType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='VOLUME_TARGET_TYPE_DURATION', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VOLUME_TARGET_TYPE_DISTANCE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VOLUME_TARGET_TYPE_CALORIES', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=176,
  serialized_end=295,
)
_sym_db.RegisterEnumDescriptor(_PBVOLUMETARGET_PBVOLYMETARGETTYPE)


_PBVOLUMETARGET = _descriptor.Descriptor(
  name='PbVolumeTarget',
  full_name='PbVolumeTarget',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='target_type', full_name='PbVolumeTarget.target_type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='duration', full_name='PbVolumeTarget.duration', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='distance', full_name='PbVolumeTarget.distance', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='calories', full_name='PbVolumeTarget.calories', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PBVOLUMETARGET_PBVOLYMETARGETTYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=34,
  serialized_end=295,
)


_PBTRAININGLOAD = _descriptor.Descriptor(
  name='PbTrainingLoad',
  full_name='PbTrainingLoad',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='training_load_val', full_name='PbTrainingLoad.training_load_val', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='recovery_time', full_name='PbTrainingLoad.recovery_time', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='carbohydrate_consumption', full_name='PbTrainingLoad.carbohydrate_consumption', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='protein_consumption', full_name='PbTrainingLoad.protein_consumption', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fat_consumption', full_name='PbTrainingLoad.fat_consumption', index=4,
      number=5, type=13, cpp_type=3, label=1,
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
  serialized_start=298,
  serialized_end=465,
)


_PBHEARTRATEZONE = _descriptor.Descriptor(
  name='PbHeartRateZone',
  full_name='PbHeartRateZone',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lower_limit', full_name='PbHeartRateZone.lower_limit', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='higher_limit', full_name='PbHeartRateZone.higher_limit', index=1,
      number=2, type=13, cpp_type=3, label=2,
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
  serialized_start=467,
  serialized_end=527,
)


_PBSPEEDZONE = _descriptor.Descriptor(
  name='PbSpeedZone',
  full_name='PbSpeedZone',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lower_limit', full_name='PbSpeedZone.lower_limit', index=0,
      number=1, type=2, cpp_type=6, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='higher_limit', full_name='PbSpeedZone.higher_limit', index=1,
      number=2, type=2, cpp_type=6, label=2,
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
  serialized_start=529,
  serialized_end=585,
)


_PBPOWERZONE = _descriptor.Descriptor(
  name='PbPowerZone',
  full_name='PbPowerZone',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='lower_limit', full_name='PbPowerZone.lower_limit', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='higher_limit', full_name='PbPowerZone.higher_limit', index=1,
      number=2, type=13, cpp_type=3, label=2,
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
  serialized_start=587,
  serialized_end=643,
)


_PBZONES = _descriptor.Descriptor(
  name='PbZones',
  full_name='PbZones',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='heart_rate_zone', full_name='PbZones.heart_rate_zone', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='speed_zone', full_name='PbZones.speed_zone', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='power_zone', full_name='PbZones.power_zone', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='heart_rate_setting_source', full_name='PbZones.heart_rate_setting_source', index=3,
      number=10, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='power_setting_source', full_name='PbZones.power_setting_source', index=4,
      number=11, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='speed_setting_source', full_name='PbZones.speed_setting_source', index=5,
      number=12, type=14, cpp_type=8, label=1,
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
  serialized_start=646,
  serialized_end=946,
)


_PBBLEMAC = _descriptor.Descriptor(
  name='PbBleMac',
  full_name='PbBleMac',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mac', full_name='PbBleMac.mac', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='PbBleMac.type', index=1,
      number=2, type=14, cpp_type=8, label=2,
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
  serialized_start=948,
  serialized_end=997,
)


_PBBLEDEVICENAME = _descriptor.Descriptor(
  name='PbBleDeviceName',
  full_name='PbBleDeviceName',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='PbBleDeviceName.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=999,
  serialized_end=1030,
)


_PBDEVICEID = _descriptor.Descriptor(
  name='PbDeviceId',
  full_name='PbDeviceId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='device_id', full_name='PbDeviceId.device_id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=1032,
  serialized_end=1063,
)


_PBRUNNINGINDEX = _descriptor.Descriptor(
  name='PbRunningIndex',
  full_name='PbRunningIndex',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='PbRunningIndex.value', index=0,
      number=1, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='calculation_time', full_name='PbRunningIndex.calculation_time', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=1065,
  serialized_end=1135,
)


_PBSPORTIDENTIFIER = _descriptor.Descriptor(
  name='PbSportIdentifier',
  full_name='PbSportIdentifier',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='PbSportIdentifier.value', index=0,
      number=1, type=4, cpp_type=4, label=2,
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
  serialized_start=1137,
  serialized_end=1171,
)


_PBONELINETEXT = _descriptor.Descriptor(
  name='PbOneLineText',
  full_name='PbOneLineText',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='PbOneLineText.text', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=1173,
  serialized_end=1202,
)


_PBMULTILINETEXT = _descriptor.Descriptor(
  name='PbMultiLineText',
  full_name='PbMultiLineText',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='PbMultiLineText.text', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=1204,
  serialized_end=1235,
)


_PBLANGUAGEID = _descriptor.Descriptor(
  name='PbLanguageId',
  full_name='PbLanguageId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='language', full_name='PbLanguageId.language', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=1237,
  serialized_end=1269,
)


_PBTRAININGSESSIONTARGETID = _descriptor.Descriptor(
  name='PbTrainingSessionTargetId',
  full_name='PbTrainingSessionTargetId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='PbTrainingSessionTargetId.value', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_modified', full_name='PbTrainingSessionTargetId.last_modified', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=1271,
  serialized_end=1355,
)


_PBTRAININGSESSIONFAVORITEID = _descriptor.Descriptor(
  name='PbTrainingSessionFavoriteId',
  full_name='PbTrainingSessionFavoriteId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='PbTrainingSessionFavoriteId.value', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_modified', full_name='PbTrainingSessionFavoriteId.last_modified', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=1357,
  serialized_end=1443,
)


_PBROUTEID = _descriptor.Descriptor(
  name='PbRouteId',
  full_name='PbRouteId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='PbRouteId.value', index=0,
      number=1, type=4, cpp_type=4, label=2,
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
  serialized_start=1445,
  serialized_end=1471,
)


_PBSWIMMINGPOOLINFO = _descriptor.Descriptor(
  name='PbSwimmingPoolInfo',
  full_name='PbSwimmingPoolInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pool_length', full_name='PbSwimmingPoolInfo.pool_length', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='swimming_pool_type', full_name='PbSwimmingPoolInfo.swimming_pool_type', index=1,
      number=2, type=14, cpp_type=8, label=2,
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
  serialized_start=1473,
  serialized_end=1564,
)


_PBTRAININGPROGRAMID = _descriptor.Descriptor(
  name='PbTrainingProgramId',
  full_name='PbTrainingProgramId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='PbTrainingProgramId.value', index=0,
      number=1, type=4, cpp_type=4, label=2,
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
  serialized_start=1566,
  serialized_end=1602,
)


_PBEVENTID = _descriptor.Descriptor(
  name='PbEventId',
  full_name='PbEventId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='PbEventId.value', index=0,
      number=1, type=4, cpp_type=4, label=2,
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
  serialized_start=1604,
  serialized_end=1630,
)

_PBVOLUMETARGET.fields_by_name['target_type'].enum_type = _PBVOLUMETARGET_PBVOLYMETARGETTYPE
_PBVOLUMETARGET.fields_by_name['duration'].message_type = types_pb2._PBDURATION
_PBVOLUMETARGET_PBVOLYMETARGETTYPE.containing_type = _PBVOLUMETARGET
_PBTRAININGLOAD.fields_by_name['recovery_time'].message_type = types_pb2._PBDURATION
_PBZONES.fields_by_name['heart_rate_zone'].message_type = _PBHEARTRATEZONE
_PBZONES.fields_by_name['speed_zone'].message_type = _PBSPEEDZONE
_PBZONES.fields_by_name['power_zone'].message_type = _PBPOWERZONE
_PBZONES.fields_by_name['heart_rate_setting_source'].enum_type = types_pb2._PBHEARTRATEZONESETTINGSOURCE
_PBZONES.fields_by_name['power_setting_source'].enum_type = types_pb2._PBPOWERZONESETTINGSOURCE
_PBZONES.fields_by_name['speed_setting_source'].enum_type = types_pb2._PBSPEEDZONESETTINGSOURCE
_PBBLEMAC.fields_by_name['type'].enum_type = types_pb2._PBMACTYPE
_PBRUNNINGINDEX.fields_by_name['calculation_time'].message_type = types_pb2._PBDURATION
_PBTRAININGSESSIONTARGETID.fields_by_name['last_modified'].message_type = types_pb2._PBSYSTEMDATETIME
_PBTRAININGSESSIONFAVORITEID.fields_by_name['last_modified'].message_type = types_pb2._PBSYSTEMDATETIME
_PBSWIMMINGPOOLINFO.fields_by_name['swimming_pool_type'].enum_type = types_pb2._PBSWIMMINGPOOLUNITS
DESCRIPTOR.message_types_by_name['PbVolumeTarget'] = _PBVOLUMETARGET
DESCRIPTOR.message_types_by_name['PbTrainingLoad'] = _PBTRAININGLOAD
DESCRIPTOR.message_types_by_name['PbHeartRateZone'] = _PBHEARTRATEZONE
DESCRIPTOR.message_types_by_name['PbSpeedZone'] = _PBSPEEDZONE
DESCRIPTOR.message_types_by_name['PbPowerZone'] = _PBPOWERZONE
DESCRIPTOR.message_types_by_name['PbZones'] = _PBZONES
DESCRIPTOR.message_types_by_name['PbBleMac'] = _PBBLEMAC
DESCRIPTOR.message_types_by_name['PbBleDeviceName'] = _PBBLEDEVICENAME
DESCRIPTOR.message_types_by_name['PbDeviceId'] = _PBDEVICEID
DESCRIPTOR.message_types_by_name['PbRunningIndex'] = _PBRUNNINGINDEX
DESCRIPTOR.message_types_by_name['PbSportIdentifier'] = _PBSPORTIDENTIFIER
DESCRIPTOR.message_types_by_name['PbOneLineText'] = _PBONELINETEXT
DESCRIPTOR.message_types_by_name['PbMultiLineText'] = _PBMULTILINETEXT
DESCRIPTOR.message_types_by_name['PbLanguageId'] = _PBLANGUAGEID
DESCRIPTOR.message_types_by_name['PbTrainingSessionTargetId'] = _PBTRAININGSESSIONTARGETID
DESCRIPTOR.message_types_by_name['PbTrainingSessionFavoriteId'] = _PBTRAININGSESSIONFAVORITEID
DESCRIPTOR.message_types_by_name['PbRouteId'] = _PBROUTEID
DESCRIPTOR.message_types_by_name['PbSwimmingPoolInfo'] = _PBSWIMMINGPOOLINFO
DESCRIPTOR.message_types_by_name['PbTrainingProgramId'] = _PBTRAININGPROGRAMID
DESCRIPTOR.message_types_by_name['PbEventId'] = _PBEVENTID

PbVolumeTarget = _reflection.GeneratedProtocolMessageType('PbVolumeTarget', (_message.Message,), dict(
  DESCRIPTOR = _PBVOLUMETARGET,
  __module__ = 'structures_pb2'
  # @@protoc_insertion_point(class_scope:PbVolumeTarget)
  ))
_sym_db.RegisterMessage(PbVolumeTarget)

PbTrainingLoad = _reflection.GeneratedProtocolMessageType('PbTrainingLoad', (_message.Message,), dict(
  DESCRIPTOR = _PBTRAININGLOAD,
  __module__ = 'structures_pb2'
  # @@protoc_insertion_point(class_scope:PbTrainingLoad)
  ))
_sym_db.RegisterMessage(PbTrainingLoad)

PbHeartRateZone = _reflection.GeneratedProtocolMessageType('PbHeartRateZone', (_message.Message,), dict(
  DESCRIPTOR = _PBHEARTRATEZONE,
  __module__ = 'structures_pb2'
  # @@protoc_insertion_point(class_scope:PbHeartRateZone)
  ))
_sym_db.RegisterMessage(PbHeartRateZone)

PbSpeedZone = _reflection.GeneratedProtocolMessageType('PbSpeedZone', (_message.Message,), dict(
  DESCRIPTOR = _PBSPEEDZONE,
  __module__ = 'structures_pb2'
  # @@protoc_insertion_point(class_scope:PbSpeedZone)
  ))
_sym_db.RegisterMessage(PbSpeedZone)

PbPowerZone = _reflection.GeneratedProtocolMessageType('PbPowerZone', (_message.Message,), dict(
  DESCRIPTOR = _PBPOWERZONE,
  __module__ = 'structures_pb2'
  # @@protoc_insertion_point(class_scope:PbPowerZone)
  ))
_sym_db.RegisterMessage(PbPowerZone)

PbZones = _reflection.GeneratedProtocolMessageType('PbZones', (_message.Message,), dict(
  DESCRIPTOR = _PBZONES,
  __module__ = 'structures_pb2'
  # @@protoc_insertion_point(class_scope:PbZones)
  ))
_sym_db.RegisterMessage(PbZones)

PbBleMac = _reflection.GeneratedProtocolMessageType('PbBleMac', (_message.Message,), dict(
  DESCRIPTOR = _PBBLEMAC,
  __module__ = 'structures_pb2'
  # @@protoc_insertion_point(class_scope:PbBleMac)
  ))
_sym_db.RegisterMessage(PbBleMac)

PbBleDeviceName = _reflection.GeneratedProtocolMessageType('PbBleDeviceName', (_message.Message,), dict(
  DESCRIPTOR = _PBBLEDEVICENAME,
  __module__ = 'structures_pb2'
  # @@protoc_insertion_point(class_scope:PbBleDeviceName)
  ))
_sym_db.RegisterMessage(PbBleDeviceName)

PbDeviceId = _reflection.GeneratedProtocolMessageType('PbDeviceId', (_message.Message,), dict(
  DESCRIPTOR = _PBDEVICEID,
  __module__ = 'structures_pb2'
  # @@protoc_insertion_point(class_scope:PbDeviceId)
  ))
_sym_db.RegisterMessage(PbDeviceId)

PbRunningIndex = _reflection.GeneratedProtocolMessageType('PbRunningIndex', (_message.Message,), dict(
  DESCRIPTOR = _PBRUNNINGINDEX,
  __module__ = 'structures_pb2'
  # @@protoc_insertion_point(class_scope:PbRunningIndex)
  ))
_sym_db.RegisterMessage(PbRunningIndex)

PbSportIdentifier = _reflection.GeneratedProtocolMessageType('PbSportIdentifier', (_message.Message,), dict(
  DESCRIPTOR = _PBSPORTIDENTIFIER,
  __module__ = 'structures_pb2'
  # @@protoc_insertion_point(class_scope:PbSportIdentifier)
  ))
_sym_db.RegisterMessage(PbSportIdentifier)

PbOneLineText = _reflection.GeneratedProtocolMessageType('PbOneLineText', (_message.Message,), dict(
  DESCRIPTOR = _PBONELINETEXT,
  __module__ = 'structures_pb2'
  # @@protoc_insertion_point(class_scope:PbOneLineText)
  ))
_sym_db.RegisterMessage(PbOneLineText)

PbMultiLineText = _reflection.GeneratedProtocolMessageType('PbMultiLineText', (_message.Message,), dict(
  DESCRIPTOR = _PBMULTILINETEXT,
  __module__ = 'structures_pb2'
  # @@protoc_insertion_point(class_scope:PbMultiLineText)
  ))
_sym_db.RegisterMessage(PbMultiLineText)

PbLanguageId = _reflection.GeneratedProtocolMessageType('PbLanguageId', (_message.Message,), dict(
  DESCRIPTOR = _PBLANGUAGEID,
  __module__ = 'structures_pb2'
  # @@protoc_insertion_point(class_scope:PbLanguageId)
  ))
_sym_db.RegisterMessage(PbLanguageId)

PbTrainingSessionTargetId = _reflection.GeneratedProtocolMessageType('PbTrainingSessionTargetId', (_message.Message,), dict(
  DESCRIPTOR = _PBTRAININGSESSIONTARGETID,
  __module__ = 'structures_pb2'
  # @@protoc_insertion_point(class_scope:PbTrainingSessionTargetId)
  ))
_sym_db.RegisterMessage(PbTrainingSessionTargetId)

PbTrainingSessionFavoriteId = _reflection.GeneratedProtocolMessageType('PbTrainingSessionFavoriteId', (_message.Message,), dict(
  DESCRIPTOR = _PBTRAININGSESSIONFAVORITEID,
  __module__ = 'structures_pb2'
  # @@protoc_insertion_point(class_scope:PbTrainingSessionFavoriteId)
  ))
_sym_db.RegisterMessage(PbTrainingSessionFavoriteId)

PbRouteId = _reflection.GeneratedProtocolMessageType('PbRouteId', (_message.Message,), dict(
  DESCRIPTOR = _PBROUTEID,
  __module__ = 'structures_pb2'
  # @@protoc_insertion_point(class_scope:PbRouteId)
  ))
_sym_db.RegisterMessage(PbRouteId)

PbSwimmingPoolInfo = _reflection.GeneratedProtocolMessageType('PbSwimmingPoolInfo', (_message.Message,), dict(
  DESCRIPTOR = _PBSWIMMINGPOOLINFO,
  __module__ = 'structures_pb2'
  # @@protoc_insertion_point(class_scope:PbSwimmingPoolInfo)
  ))
_sym_db.RegisterMessage(PbSwimmingPoolInfo)

PbTrainingProgramId = _reflection.GeneratedProtocolMessageType('PbTrainingProgramId', (_message.Message,), dict(
  DESCRIPTOR = _PBTRAININGPROGRAMID,
  __module__ = 'structures_pb2'
  # @@protoc_insertion_point(class_scope:PbTrainingProgramId)
  ))
_sym_db.RegisterMessage(PbTrainingProgramId)

PbEventId = _reflection.GeneratedProtocolMessageType('PbEventId', (_message.Message,), dict(
  DESCRIPTOR = _PBEVENTID,
  __module__ = 'structures_pb2'
  # @@protoc_insertion_point(class_scope:PbEventId)
  ))
_sym_db.RegisterMessage(PbEventId)


# @@protoc_insertion_point(module_scope)