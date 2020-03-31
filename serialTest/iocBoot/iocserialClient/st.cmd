#!../../bin/linux-arm/serialClient

## You may have to change serialClient to something else
## everywhere it appears in this file

< envPaths

cd "${TOP}"

epicsEnvSet "STREAM_PROTOCOL_PATH" "../../proto"

## Register all support components
dbLoadDatabase "dbd/serialClient.dbd"
serialClient_registerRecordDeviceDriver pdbbase

drvAsynSerialPortConfigure "UART" "/dev/ttyS0"

asynSetOption("UART", 0, "baud", "9600")
asynSetOption("UART", 0, "bits", "8")
asynSetOption("UART", 0, "parity", "none")

## Load record instances
#dbLoadRecords("db/xxx.db","user=ctrluserHost")

dbLoadRecords("db/client.db")

cd "${TOP}/iocBoot/${IOC}"
iocInit

## Start any sequence programs
#seq sncxxx,"user=ctrluserHost"
