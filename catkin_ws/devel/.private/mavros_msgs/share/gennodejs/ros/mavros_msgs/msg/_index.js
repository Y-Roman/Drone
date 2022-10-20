
"use strict";

let ESCStatus = require('./ESCStatus.js');
let FileEntry = require('./FileEntry.js');
let HilSensor = require('./HilSensor.js');
let LandingTarget = require('./LandingTarget.js');
let GPSRAW = require('./GPSRAW.js');
let HilActuatorControls = require('./HilActuatorControls.js');
let Mavlink = require('./Mavlink.js');
let LogEntry = require('./LogEntry.js');
let PositionTarget = require('./PositionTarget.js');
let OnboardComputerStatus = require('./OnboardComputerStatus.js');
let Waypoint = require('./Waypoint.js');
let Tunnel = require('./Tunnel.js');
let AttitudeTarget = require('./AttitudeTarget.js');
let DebugValue = require('./DebugValue.js');
let GPSINPUT = require('./GPSINPUT.js');
let MagnetometerReporter = require('./MagnetometerReporter.js');
let Vibration = require('./Vibration.js');
let RTKBaseline = require('./RTKBaseline.js');
let GlobalPositionTarget = require('./GlobalPositionTarget.js');
let ESCStatusItem = require('./ESCStatusItem.js');
let Trajectory = require('./Trajectory.js');
let HomePosition = require('./HomePosition.js');
let CameraImageCaptured = require('./CameraImageCaptured.js');
let ESCTelemetry = require('./ESCTelemetry.js');
let OverrideRCIn = require('./OverrideRCIn.js');
let CamIMUStamp = require('./CamIMUStamp.js');
let ExtendedState = require('./ExtendedState.js');
let ParamValue = require('./ParamValue.js');
let HilStateQuaternion = require('./HilStateQuaternion.js');
let WaypointReached = require('./WaypointReached.js');
let NavControllerOutput = require('./NavControllerOutput.js');
let MountControl = require('./MountControl.js');
let ManualControl = require('./ManualControl.js');
let CompanionProcessStatus = require('./CompanionProcessStatus.js');
let Altitude = require('./Altitude.js');
let CommandCode = require('./CommandCode.js');
let State = require('./State.js');
let OpticalFlowRad = require('./OpticalFlowRad.js');
let RTCM = require('./RTCM.js');
let RCIn = require('./RCIn.js');
let ESCInfoItem = require('./ESCInfoItem.js');
let HilGPS = require('./HilGPS.js');
let TimesyncStatus = require('./TimesyncStatus.js');
let WheelOdomStamped = require('./WheelOdomStamped.js');
let Param = require('./Param.js');
let RadioStatus = require('./RadioStatus.js');
let ESCInfo = require('./ESCInfo.js');
let BatteryStatus = require('./BatteryStatus.js');
let ADSBVehicle = require('./ADSBVehicle.js');
let RCOut = require('./RCOut.js');
let LogData = require('./LogData.js');
let ESCTelemetryItem = require('./ESCTelemetryItem.js');
let GPSRTK = require('./GPSRTK.js');
let StatusText = require('./StatusText.js');
let HilControls = require('./HilControls.js');
let EstimatorStatus = require('./EstimatorStatus.js');
let VehicleInfo = require('./VehicleInfo.js');
let PlayTuneV2 = require('./PlayTuneV2.js');
let TerrainReport = require('./TerrainReport.js');
let WaypointList = require('./WaypointList.js');
let ActuatorControl = require('./ActuatorControl.js');
let VFR_HUD = require('./VFR_HUD.js');
let Thrust = require('./Thrust.js');

module.exports = {
  ESCStatus: ESCStatus,
  FileEntry: FileEntry,
  HilSensor: HilSensor,
  LandingTarget: LandingTarget,
  GPSRAW: GPSRAW,
  HilActuatorControls: HilActuatorControls,
  Mavlink: Mavlink,
  LogEntry: LogEntry,
  PositionTarget: PositionTarget,
  OnboardComputerStatus: OnboardComputerStatus,
  Waypoint: Waypoint,
  Tunnel: Tunnel,
  AttitudeTarget: AttitudeTarget,
  DebugValue: DebugValue,
  GPSINPUT: GPSINPUT,
  MagnetometerReporter: MagnetometerReporter,
  Vibration: Vibration,
  RTKBaseline: RTKBaseline,
  GlobalPositionTarget: GlobalPositionTarget,
  ESCStatusItem: ESCStatusItem,
  Trajectory: Trajectory,
  HomePosition: HomePosition,
  CameraImageCaptured: CameraImageCaptured,
  ESCTelemetry: ESCTelemetry,
  OverrideRCIn: OverrideRCIn,
  CamIMUStamp: CamIMUStamp,
  ExtendedState: ExtendedState,
  ParamValue: ParamValue,
  HilStateQuaternion: HilStateQuaternion,
  WaypointReached: WaypointReached,
  NavControllerOutput: NavControllerOutput,
  MountControl: MountControl,
  ManualControl: ManualControl,
  CompanionProcessStatus: CompanionProcessStatus,
  Altitude: Altitude,
  CommandCode: CommandCode,
  State: State,
  OpticalFlowRad: OpticalFlowRad,
  RTCM: RTCM,
  RCIn: RCIn,
  ESCInfoItem: ESCInfoItem,
  HilGPS: HilGPS,
  TimesyncStatus: TimesyncStatus,
  WheelOdomStamped: WheelOdomStamped,
  Param: Param,
  RadioStatus: RadioStatus,
  ESCInfo: ESCInfo,
  BatteryStatus: BatteryStatus,
  ADSBVehicle: ADSBVehicle,
  RCOut: RCOut,
  LogData: LogData,
  ESCTelemetryItem: ESCTelemetryItem,
  GPSRTK: GPSRTK,
  StatusText: StatusText,
  HilControls: HilControls,
  EstimatorStatus: EstimatorStatus,
  VehicleInfo: VehicleInfo,
  PlayTuneV2: PlayTuneV2,
  TerrainReport: TerrainReport,
  WaypointList: WaypointList,
  ActuatorControl: ActuatorControl,
  VFR_HUD: VFR_HUD,
  Thrust: Thrust,
};
