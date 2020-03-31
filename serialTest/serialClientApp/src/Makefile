TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#=============================
# Build the IOC application

PROD_IOC = serialClient
# serialClient.dbd will be created and installed
DBD += serialClient.dbd

# serialClient.dbd will be made up from these files:
serialClient_DBD += base.dbd

# Include dbd files from all support applications:
#serialClient_DBD += xxx.dbd
serialClient_DBD += stream.dbd
serialClient_DBD += asyn.dbd
serialClient_DBD += drvAsynSerialPort.dbd

# Add all the support libraries needed by this IOC
#serialClient_LIBS += xxx
serialClient_LIBS += stream
serialClient_LIBS += asyn

# serialClient_registerRecordDeviceDriver.cpp derives from serialClient.dbd
serialClient_SRCS += serialClient_registerRecordDeviceDriver.cpp

# Build the main IOC entry point on workstation OSs.
serialClient_SRCS_DEFAULT += serialClientMain.cpp
serialClient_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
#serialClient_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Finally link to the EPICS Base libraries
serialClient_LIBS += $(EPICS_BASE_IOC_LIBS)

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

