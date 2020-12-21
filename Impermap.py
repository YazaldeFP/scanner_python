import nmap
N = PortScanner()
Alvo=input("[✓]Yazalde[✓]==>> Entre com o teu alvo[Site/Maquina[IP/URL]]")
Port=input("[✓]Yazalde[✓]==>> Entre com a porta [porta padrao[4444]]: ")
Port=4444
N.scan(Alvo, Port)
for host in N.all_hosts():
    hot=(host, N[host].hostname())
    Status=(N[host].state())
    print(f'''
             [✓][✓][✓] Yazalde Felimone Pinto™ [✓][✓][✓]
        \033[1;92m[✓]Me apoie na vaquinha a ter um pc[✓]\033[m
             
             ~~~~~~~~~~~~~~~~~~~~~Scanner~~~~~~~~~~~~~~~~~~
             [+]Hosts: \033[1;91m{hot}
             [+]Status: \033[1;91m{Status}
          ''')
    for proto in N[host].all_protocols():
        print(f'''
                ~~~~~~~~~~~~~~~~~~Protocol~~~~~~~~~~~~~~~~~~
                [+]Protocol:{proto}
                ''')
        lport = N[host][proto].keys()
        lport = list(lport)
        lport.sort()
        for port in lport:
            pota=(port, N[host][proto][port]['state'])
            print('''
                    ~~~~~~~~~~~~~~Port~~~~~~~~~~~~~~~~~~~~~~
                    [+]Porta: {pota}
                  ''')

