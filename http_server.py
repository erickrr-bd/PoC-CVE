#! /usr/bin/env python3.12

"""
Author: Erick Roberto Rodriguez Rodriguez
Email: erodriguez@tekium.mx, erickrr.tbd93@gmail.com
GitHub: https://github.com/erickrr-bd/libPyElk
Simple HTTP Server - June 2025
"""
import argparse
import http.server
import socketserver

RED = "\33[91m"
GREEN = "\033[32m"
END = "\033[0m"

BANNER = f"""
{GREEN} 
██╗  ██╗████████╗████████╗██████╗       ███████╗███████╗██████╗ ██╗   ██╗███████╗██████╗ 
██║  ██║╚══██╔══╝╚══██╔══╝██╔══██╗      ██╔════╝██╔════╝██╔══██╗██║   ██║██╔════╝██╔══██╗
███████║   ██║      ██║   ██████╔╝█████╗███████╗█████╗  ██████╔╝██║   ██║█████╗  ██████╔╝
██╔══██║   ██║      ██║   ██╔═══╝ ╚════╝╚════██║██╔══╝  ██╔══██╗╚██╗ ██╔╝██╔══╝  ██╔══██╗
██║  ██║   ██║      ██║   ██║           ███████║███████╗██║  ██║ ╚████╔╝ ███████╗██║  ██║
╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚═╝           ╚══════╝╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝                                                                                                                                                                                                                                                                                                                                                                                                                                                             
By Erick Rodríguez                                                                                                                                                                                              
{END}
"""

if __name__ == "__main__":
    print(BANNER)

    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", default = "80", help = "Server HTTP port")
    args = parser.parse_args()

    print(f"[*] Port: {args.port}\n")

    handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("", int(args.port)), handler) as httpd:
        print(f"Server listening on port: {args.port}")
        httpd.serve_forever()
