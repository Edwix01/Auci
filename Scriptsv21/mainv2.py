import bridge_id
import stp_info
import com_conex
import des_disp
import des_int_act
import gr
import map_int
import stp_blk
import verstp
import time 
import tree

# Ingreso de Parametros - Comunidad SNMP, Direcciones IP
comunidad = "$1$5.v/c/$"
direc = des_disp.in_des()

tif1 = time.time()
#Fase 1
#Detección de interfaces activas 
#d = (des_int_act.in_act(direc,comunidad))
#direc = d.keys() #Direcciones IP Filtradas
tff1 = time.time()
print("Tiempo en fase 1: ",(tff1-tif1))


tif2 = time.time()
#Fase 2
#Informacion STP
# Bridge ID, Designed Bridge
b_id = bridge_id.bri_id(direc,comunidad)
st_inf = stp_info.stp_inf(direc,comunidad)
tff2 = time.time()
print("Tiempo en fase 2: ",(tff2-tif2))
print(b_id)
print(st_inf)
tif3 = time.time()
#Fase 3
#Identificación de Conexiones
l = com_conex.b_conex(direc,b_id,st_inf)
print(l)
tff3 = time.time()
print("Tiempo en fase 3: ",(tff3-tif3))

#Filtro de Switches sin conexiones
"""
l1 = []
for tupla in l:
    for elemento in tupla:
        nodo_principal = elemento.split('.')[0]
        if nodo_principal not in l1:
            l1.append(nodo_principal)
"""
tif4 = time.time()
#Fase 4
#Deteccion de puertos habilitados con stp
#Detección de puertos bloqueados por stp
nf = verstp.obtener_numeros_despues_del_punto(l)
nodb=stp_blk.stp_status(direc,nf,comunidad)
tff4 = time.time()
print("Tiempo en fase 4: ",(tff4-tif4))


tif5 = time.time()
#Fase 5
#Creación del grafo
info_int = map_int.ma_int(direc,comunidad)
print(info_int)

info_int = map_int.ma_int(direc,comunidad)
print(info_int)

interconnections = tree.connection_tree_web(l,info_int)
discovered_hosts = ['switch3', 'switch4', 'switch5', 'switch6', 'switch7', 'switch8','switch9', 'switch10', 'switch11', 'switch12','switch13', 'switch14', 'switch15', 'switch16','switch17', 'switch18', 'switch19', 'switch20','switch21']
print(interconnections)
OUTPUT_TOPOLOGY_FILENAME = 'topology.js'
TOPOLOGY_FILE_PATH = r"C:\Users\User\OneDrive\Tesis 1\Python\Automatizacion_Red_2024\Scriptsv21\app\topology.js"
TOPOLOGY_FILE_HEAD = f"\n\nvar topologyData = "
TOPOLOGY_DICT = tree.generate_topology_json(discovered_hosts, interconnections)
tree.write_topology_file(TOPOLOGY_DICT,TOPOLOGY_FILE_HEAD,TOPOLOGY_FILE_PATH )

grafo = gr.crear_grafo(direc, l, info_int,nodb)
tff5 = time.time()
print("Tiempo en fase 5: ",(tff5-tif5))
gr.dibujar_grafo(grafo)

