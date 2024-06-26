from pysnmp.entity.rfc3413.oneliner import cmdgen

cmdGen = cmdgen.CommandGenerator()

def stp_status(direc,stpi,comunidad):
    sl = []
    for server_ip in direc:
        errorIndication, errorStatus, errorIndex, varBindTable = cmdGen.bulkCmd(
            cmdgen.CommunityData(comunidad),
            cmdgen.UdpTransportTarget((server_ip, 161)),
            0,25,
            '1.3.6.1.2.1.17.2.15.1.3'
        )
        for varBindTableRow in varBindTable:
            for name, val in varBindTableRow:
                if server_ip.split(".")[-1] in stpi.keys():
                    p = str(name).split(".")[-1]
                    lp = stpi[server_ip.split(".")[-1]]
                    if p in lp:
                        if val.prettyPrint() == "2":
                            sl.append(server_ip.split(".")[-1]+"."+p)
    return sl