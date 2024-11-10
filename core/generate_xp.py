#! /usr/bin/python

from __future__ import print_function

import collections
from collections.abc import Iterable


XP_TYPE = "xpType"
# CLIENT_PCAP = "clientPcap"
# SERVER_PCAP = "serverPcap"
# SNAPLEN_PCAP = "snaplenPcap"
# SCHEDULER = "sched"
# SCHEDULER_CLIENT = "schedc"
# SCHEDULER_SERVER = "scheds"
# CC = "serverCcAlgorithm"
# KERNEL_PATH_MANAGER_CLIENT = "kpmc"
# KERNEL_PATH_MANAGER_SERVER = "kpms"
# RMEM = "rmem"
# WMEM = "wmem"
# AUTOCORK = "autocork"
# EARLY_RETRANS = "earlyRetrans"
''' Specific to quiche '''
SIZE = "quicheSize"
CLIENT_FLAGS = "clientFlags"
SERVER_FLAGS = "serverFlags"
ENV = "env"

# Server-specific parameters
CERT_PATH = "serverCertPath"
KEY_PATH = "serverKeyPath"
LISTEN_ADDR = "serverListenAddr"
ROOT_DIR = "serverRootDir"
INDEX_FILE = "serverIndexFile"
NAME = "serverName"
MAX_DATA = "serverMaxData"
MAX_WINDOW = "serverMaxWindow"
MAX_STREAM_DATA = "serverMaxStreamData"
MAX_STREAM_WINDOW = "serverMaxStreamWindow"
MAX_STREAMS_BIDI = "serverMaxStreamsBidi"
MAX_STREAMS_UNI = "serverMaxStreamsUni"
IDLE_TIMEOUT = "serverIdleTimeout"
CC_ALGORITHM = "serverCcAlgorithm"
ENABLE_EARLY_DATA = "serverEnableEarlyData"
ENABLE_RETRY = "serverEnableRetry"
DISABLE_GREASE = "serverDisableGrease"
HTTP_VERSION = "serverHttpVersion"
INITIAL_MAX_PATH_ID_SERVER = "initialMaxPathIdServer"
INITIAL_MAX_PATH_ID_CLIENT = "initialMaxPathIdClient"

# Client-specific parameters
METHOD = "clientMethod"
BODY = "clientBody"
MAX_DATA_CLIENT = "clientMaxData"
MAX_WINDOW_CLIENT = "clientMaxWindow"
MAX_STREAM_DATA_CLIENT = "clientMaxStreamData"
MAX_STREAM_WINDOW_CLIENT = "clientMaxStreamWindow"
MAX_STREAMS_BIDI_CLIENT = "clientMaxStreamsBidi"
MAX_STREAMS_UNI_CLIENT = "clientMaxStreamsUni"
IDLE_TIMEOUT_CLIENT = "clientIdleTimeout"
WIRE_VERSION = "clientWireVersion"
DGRAM_PROTO = "clientDgramProto"
DGRAM_COUNT = "clientDgramCount"
DGRAM_DATA = "clientDgramData"
DUMP_PACKETS = "clientDumpPackets"
DUMP_RESPONSES = "clientDumpResponses"
DUMP_JSON = "clientDumpJson"
MAX_JSON_PAYLOAD = "clientMaxJsonPayload"
CONNECT_TO = "clientConnectTo"
TRUST_CA = "clientTrustCA"
CC_ALGORITHM_CLIENT = "clientCcAlgorithm"
MAX_ACTIVE_CIDS = "clientMaxActiveCIDs"
PERFORM_MIGRATION = "clientPerformMigration"
SOURCE_PORT = "clientSourcePort"
INITIAL_CWND_PACKETS = "clientInitialCwndPackets"
SESSION_FILE = "clientSessionFile"


""" XP TYPES """
HTTPS = "https"
QUIC = "quic"
QUICREQRES = "quicreqres"
QUICHE = "quiche"

""" Specific to https """
# HTTPS_FILE = "file"
# HTTPS_RANDOM_SIZE = "file_size"

""" Specific to all QUIC experiences """
QUIC_MULTIPATH = "quicMultipath"

""" Specific to QUIC reqres experiences """
QUICREQRES_RUN_TIME = "quicReqresRunTime"

""" Default values """
DEFAULT_XP_TYPE = QUICHE
DEFAULT_CLIENT_PCAP = "yes"
DEFAULT_SERVER_PCAP = "no"
DEFAULT_SNAPLEN_PCAP = "100"
DEFAULT_SCHEDULER = "default"
DEFAULT_CC = "olia"
DEFAULT_KERNEL_PATH_MANAGER_CLIENT = "fullmesh"
DEFAULT_KERNEL_PATH_MANAGER_SERVER = "fullmesh"
DEFAULT_EARLY_RETRANS = "3"

""" Default values for specific fields to https """
DEFAULT_HTTPS_FILE = "random"
DEFAULT_HTTPS_RANDOM_SIZE = "3456"      # Changed this to make the related error more visible for debugging purpose

""" Default values for specific fields to all QUIC experiences """
DEFAULT_QUIC_MULTIPATH = "0"

""" Default values for specific fields to QUIC siri """
DEFAULT_QUICREQRES_RUN_TIME = "30"


def fillHttpsInfo(xpFile, xpDict):
    print(HTTPS_FILE + ":" + str(xpDict.get(HTTPS_FILE, DEFAULT_HTTPS_FILE)), file=xpFile)
    print(HTTPS_RANDOM_SIZE + ":" + str(xpDict.get(HTTPS_RANDOM_SIZE, DEFAULT_HTTPS_RANDOM_SIZE)), file=xpFile)


def fillCommonQUICInfo(xpFile, xpDict):
    print(QUIC_MULTIPATH + ":" + str(xpDict.get(QUIC_MULTIPATH, DEFAULT_QUIC_MULTIPATH)), file=xpFile)


def fillQUICInfo(xpFile, xpDict):
    fillCommonQUICInfo(xpFile, xpDict)
    print(HTTPS_FILE + ":" + str(xpDict.get(HTTPS_FILE, DEFAULT_HTTPS_FILE)), file=xpFile)
    print(HTTPS_RANDOM_SIZE + ":" + str(xpDict.get(HTTPS_RANDOM_SIZE, DEFAULT_HTTPS_RANDOM_SIZE)), file=xpFile)


def fillQUICReqresInfo(xpFile, xpDict):
    fillCommonQUICInfo(xpFile, xpDict)
    print(QUICREQRES_RUN_TIME + ":" + str(xpDict.get(QUICREQRES_RUN_TIME, DEFAULT_QUICREQRES_RUN_TIME)), file=xpFile)


def generateXpFile(xpFilename, xpDict):
    xpFile = open(xpFilename, 'w')
    xpType = xpDict.get(XP_TYPE, DEFAULT_XP_TYPE)
    """ First set common information for any experience """
    print(XP_TYPE + ":" + xpType, file=xpFile)
    # print(CLIENT_PCAP + ":" + xpDict.get(CLIENT_PCAP, DEFAULT_CLIENT_PCAP), file=xpFile)
    # print(SERVER_PCAP + ":" + xpDict.get(SERVER_PCAP, DEFAULT_SERVER_PCAP), file=xpFile)
    # print(SNAPLEN_PCAP + ":" + xpDict.get(SNAPLEN_PCAP, DEFAULT_SNAPLEN_PCAP), file=xpFile)
    # if SCHEDULER_CLIENT in xpDict and SCHEDULER_SERVER in xpDict:
    #     print(SCHEDULER_CLIENT + ":" + str(xpDict[SCHEDULER_CLIENT]), file=xpFile)
    #     print(SCHEDULER_SERVER + ":" + str(xpDict[SCHEDULER_SERVER]), file=xpFile)
    # else:
    #     print(SCHEDULER + ":" + xpDict.get(SCHEDULER, DEFAULT_SCHEDULER), file=xpFile)
    # print(CC + ":" + xpDict.get(CC, DEFAULT_CC), file=xpFile)
    # print(KERNEL_PATH_MANAGER_CLIENT + ":" + xpDict.get(KERNEL_PATH_MANAGER_CLIENT, DEFAULT_KERNEL_PATH_MANAGER_CLIENT), file=xpFile)
    # print(KERNEL_PATH_MANAGER_SERVER + ":" + xpDict.get(KERNEL_PATH_MANAGER_SERVER, DEFAULT_KERNEL_PATH_MANAGER_SERVER), file=xpFile)
    # print(EARLY_RETRANS + ":" + str(xpDict.get(EARLY_RETRANS, DEFAULT_EARLY_RETRANS)), file=xpFile)
    """ Set rmem if defined (assume as string, int or iterable) """
    # if RMEM in xpDict:
    #     rmemRaw = xpDict[RMEM]
    #     if isinstance(rmemRaw, int):
    #         rmem = (rmemRaw, rmemRaw, rmemRaw)
    #     elif isinstance(rmemRaw, str) or (isinstance(rmemRaw, Iterable) and len(rmemRaw) == 3):
    #         # Assume it's ok
    #         rmem = rmemRaw
    #     else:
    #         raise Exception("Formatting error for rmem: " + str(rmemRaw))

    #     print(RMEM + ":" + str(rmem[0]), str(rmem[1]), str(rmem[2]), file=xpFile)
    if xpType == QUICHE:
        # Server specific parameters
        print("env:" + xpDict.get("env", "RUST_BACKTRACE=full RUST_LOG=info"), file=xpFile)
        print("quicheSize:" + xpDict.get("quicheSize","2345"), file=xpFile)
        print("serverFlags:"+xpDict.get("serverFlags", "--disable-gso"), file=xpFile)
        print("serverCertPath:" + xpDict.get("serverCertPath", "/path/to/cert.crt"), file=xpFile)
        print("serverKeyPath:" + xpDict.get("serverKeyPath", "/path/to/key.key"), file=xpFile)
        print("serverRootDir:" + xpDict.get("serverRootDir", "/path/to/root"), file=xpFile)
        print("serverIndexFile:" + xpDict.get("serverIndexFile", "index.html"), file=xpFile)
        print("serverName:" + xpDict.get("serverName", "quic.tech"), file=xpFile)
        print("serverMaxData:" + str(xpDict.get("serverMaxData", 10000000)), file=xpFile)
        print("serverMaxWindow:" + str(xpDict.get("serverMaxWindow", 25165824)), file=xpFile)
        print("serverMaxStreamData:" + str(xpDict.get("serverMaxStreamData", 1000000)), file=xpFile)
        print("serverMaxStreamWindow:" + str(xpDict.get("serverMaxStreamWindow", 16777216)), file=xpFile)
        print("serverMaxStreamsBidi:" + str(xpDict.get("serverMaxStreamsBidi", 100)), file=xpFile)
        print("serverMaxStreamsUni:" + str(xpDict.get("serverMaxStreamsUni", 100)), file=xpFile)
        print("serverIdleTimeout:" + str(xpDict.get("serverIdleTimeout", 30000)), file=xpFile)
        print("serverCcAlgorithm:" + xpDict.get("serverCcAlgorithm"), file=xpFile)      # Removed the default CC to monitor CC erroneous settings
        print("serverEnableEarlyData:" + str(xpDict.get("serverEnableEarlyData", True)), file=xpFile)
        print("serverEnableRetry:" + str(xpDict.get("serverEnableRetry", False)), file=xpFile)
        print("serverDisableGrease:" + str(xpDict.get("serverDisableGrease", False)), file=xpFile)
        print("serverHttpVersion:" + xpDict.get("serverHttpVersion", "HTTP/3"), file=xpFile)

        # Client specific parameters
        print("clientFlags:" + xpDict.get("clientFlags", "GET"), file=xpFile)
        print("clientMethod:" + xpDict.get("clientMethod", "GET"), file=xpFile)
        print("clientMaxData:" + str(xpDict.get("clientMaxData", 10000000)), file=xpFile)
        print("clientMaxWindow:" + str(xpDict.get("clientMaxWindow", 25165824)), file=xpFile)
        print("clientMaxStreamData:" + str(xpDict.get("clientMaxStreamData", 1000000)), file=xpFile)
        print("clientMaxStreamWindow:" + str(xpDict.get("clientMaxStreamWindow", 16777216)), file=xpFile)
        print("clientMaxStreamsBidi:" + str(xpDict.get("clientMaxStreamsBidi", 100)), file=xpFile)
        print("clientMaxStreamsUni:" + str(xpDict.get("clientMaxStreamsUni", 100)), file=xpFile)
        print("clientIdleTimeout:" + str(xpDict.get("clientIdleTimeout", 30000)), file=xpFile)
        print("clientWireVersion:" + xpDict.get("clientWireVersion", "babababa"), file=xpFile)
        print("clientDgramProto:" + xpDict.get("clientDgramProto", "none"), file=xpFile)
        print("clientDgramCount:" + str(xpDict.get("clientDgramCount", 0)), file=xpFile)
        print("clientDgramData:" + xpDict.get("clientDgramData", "quack"), file=xpFile)
        print("clientDumpJson:" + str(xpDict.get("clientDumpJson", False)), file=xpFile)
        print("clientMaxJsonPayload:" + str(xpDict.get("clientMaxJsonPayload", 10000)), file=xpFile)
        print("clientCcAlgorithm:" + str(xpDict.get("clientCcAlgorithm")), file=xpFile)
        print("clientMaxActiveCIDs:" + str(xpDict.get("clientMaxActiveCIDs", 2)), file=xpFile)
        print("clientPerformMigration:" + str(xpDict.get("clientPerformMigration", False)), file=xpFile)
        print("clientSourcePort:" + str(xpDict.get("clientSourcePort", 0)), file=xpFile)
        print("clientInitialCwndPackets:" + str(xpDict.get("clientInitialCwndPackets", 10)), file=xpFile)
        print("initialMaxPathIdClient:" + str(xpDict.get("initialMaxPathIdClient", 2)), file=xpFile)
        print("initialMaxPathIdServer:" + str(xpDict.get("initialMaxPathIdServer", 2)), file=xpFile)
    elif xpType == HTTPS:
        fillHttpsInfo(xpFile, xpDict)
    elif xpType == QUIC:
        fillQUICInfo(xpFile, xpDict)
    elif xpType == QUICREQRES:
        fillQUICReqresInfo(xpFile, xpDict)
    else:
        raise NotImplementedError("Experience not yet implemented: " + xpType)

    xpFile.close()


if __name__ == '__main__':
    xpHttpsDict = {
        XP_TYPE: QUIC,
        HTTPS_RANDOM_SIZE: "2048"
    }
    generateXpFile("my_quic_xp", xpHttpsDict)
