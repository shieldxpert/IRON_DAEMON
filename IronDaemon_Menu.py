# Created by ShieldXpert

#!/usr/bin/env python3
import socket
import sys
import time
from smb.SMBConnection import SMBConnection

def detectar_puerto(ip):
    for puerto in [445, 139]:
        try:
            with socket.create_connection((ip, puerto), timeout=2):
                return puerto
        except:
            continue
    return None

def obtener_info_os(conn):
    return conn.remote_name, conn.remote_os

def obtener_lista_usuarios(conn):
    try:
        return [usuario.name for usuario in conn.listUsers()]
    except:
        return []

def obtener_lista_grupos(conn):
    try:
        return [grupo.name for grupo in conn.listGroups()]
    except:
        return []

def obtener_lista_recursos_compartidos(conn):
    try:
        return [recurso.name for recurso in conn.listShares()]
    except:
        return []

def mostrar_barra_progreso():
    barra = ''
    print("\n[IRON DAEMON] Escaneando el objetivo...\n")
    for i in range(30):
        barra += '█'
        sys.stdout.write(f"\r\033[91m[{barra:<30}]\033[0m")
        sys.stdout.flush()
        time.sleep(0.05)
    print("\n")

def enumerar_conexion(ip, usuario, contrasena):
    puerto = detectar_puerto(ip)
    if puerto is None:
        print("[ERROR] No se pudo conectar al puerto 139 o 445.")
        return False

    conn = SMBConnection(usuario, contrasena, "IRON_DAEMON", ip, use_ntlm_v2=True)
    try:
        if not conn.connect(ip, puerto):
            print("[!] Conexión fallida con usuario:", usuario)
            return False
    except Exception as e:
        print(f"[ERROR] Conexión fallida: {e}")
        return False

    print(f"\n[IRON DAEMON] Conectado a {ip}:{puerto} como '{usuario}'\n")
    nombre_servidor, sistema_operativo = obtener_info_os(conn)
    print(f"[+] Nombre del servidor: {nombre_servidor}")
    print(f"[+] Sistema operativo: {sistema_operativo}")

    print("\n[+] Usuarios detectados:")
    for u in obtener_lista_usuarios(conn) or ["[Sin acceso]"]:
        print("  -", u)

    print("\n[+] Grupos encontrados:")
    for g in obtener_lista_grupos(conn) or ["[Sin acceso]"]:
        print("  -", g)

    print("\n[+] Recursos compartidos disponibles:")
    for r in obtener_lista_recursos_compartidos(conn) or ["[Sin acceso]"]:
        print("  -", r)

    return True

def main():
    print("Created by ShieldXpert")
    print("IRON DAEMON - SMB Enumerator\n")

    ip = input("IP del objetivo: ").strip()

    mostrar_barra_progreso()

    print("[INFO] Intentando acceso anónimo...")
    if not enumerar_conexion(ip, '', ''):
        print("\n[!] El acceso anónimo falló. Se requieren credenciales.")
        user = input("Usuario SMB: ").strip()
        pwd = input("Contraseña SMB: ").strip()
        enumerar_conexion(ip, user, pwd)

if __name__ == '__main__':
    main()
