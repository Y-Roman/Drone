
"use strict";

let MessageInterval = require('./MessageInterval.js')
let ParamPush = require('./ParamPush.js')
let CommandTriggerControl = require('./CommandTriggerControl.js')
let FileOpen = require('./FileOpen.js')
let CommandTriggerInterval = require('./CommandTriggerInterval.js')
let ParamGet = require('./ParamGet.js')
let WaypointClear = require('./WaypointClear.js')
let FileChecksum = require('./FileChecksum.js')
let SetMavFrame = require('./SetMavFrame.js')
let CommandAck = require('./CommandAck.js')
let FileRename = require('./FileRename.js')
let WaypointSetCurrent = require('./WaypointSetCurrent.js')
let LogRequestEnd = require('./LogRequestEnd.js')
let VehicleInfoGet = require('./VehicleInfoGet.js')
let CommandInt = require('./CommandInt.js')
let WaypointPush = require('./WaypointPush.js')
let FileRead = require('./FileRead.js')
let FileTruncate = require('./FileTruncate.js')
let MountConfigure = require('./MountConfigure.js')
let CommandHome = require('./CommandHome.js')
let FileWrite = require('./FileWrite.js')
let LogRequestList = require('./LogRequestList.js')
let StreamRate = require('./StreamRate.js')
let ParamPull = require('./ParamPull.js')
let FileMakeDir = require('./FileMakeDir.js')
let SetMode = require('./SetMode.js')
let CommandTOL = require('./CommandTOL.js')
let LogRequestData = require('./LogRequestData.js')
let WaypointPull = require('./WaypointPull.js')
let CommandVtolTransition = require('./CommandVtolTransition.js')
let FileClose = require('./FileClose.js')
let CommandBool = require('./CommandBool.js')
let FileList = require('./FileList.js')
let FileRemoveDir = require('./FileRemoveDir.js')
let CommandLong = require('./CommandLong.js')
let ParamSet = require('./ParamSet.js')
let FileRemove = require('./FileRemove.js')

module.exports = {
  MessageInterval: MessageInterval,
  ParamPush: ParamPush,
  CommandTriggerControl: CommandTriggerControl,
  FileOpen: FileOpen,
  CommandTriggerInterval: CommandTriggerInterval,
  ParamGet: ParamGet,
  WaypointClear: WaypointClear,
  FileChecksum: FileChecksum,
  SetMavFrame: SetMavFrame,
  CommandAck: CommandAck,
  FileRename: FileRename,
  WaypointSetCurrent: WaypointSetCurrent,
  LogRequestEnd: LogRequestEnd,
  VehicleInfoGet: VehicleInfoGet,
  CommandInt: CommandInt,
  WaypointPush: WaypointPush,
  FileRead: FileRead,
  FileTruncate: FileTruncate,
  MountConfigure: MountConfigure,
  CommandHome: CommandHome,
  FileWrite: FileWrite,
  LogRequestList: LogRequestList,
  StreamRate: StreamRate,
  ParamPull: ParamPull,
  FileMakeDir: FileMakeDir,
  SetMode: SetMode,
  CommandTOL: CommandTOL,
  LogRequestData: LogRequestData,
  WaypointPull: WaypointPull,
  CommandVtolTransition: CommandVtolTransition,
  FileClose: FileClose,
  CommandBool: CommandBool,
  FileList: FileList,
  FileRemoveDir: FileRemoveDir,
  CommandLong: CommandLong,
  ParamSet: ParamSet,
  FileRemove: FileRemove,
};
