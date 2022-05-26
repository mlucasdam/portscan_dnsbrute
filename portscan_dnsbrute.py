import socket
import dns.resolver

ports = []

for port in ports:
    client = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout (15)
    code = client.connect_ex(("#ip", port))
    if code == 0:
        print (port, "aberta")
        
        
        
res = dns.resolver.Resolver ()
arquivo = open ("/home/kali/Desktop/Programacao/worldlist.txt", "r")
subdominios = arquivo.read().splitlines()

alvo = "webmail.jovemnerd.com.br"
for subdominio in subdominios:
    try:
        sub_alvo = subdominio + "." + alvo
        resultado = res.resolve(alvo, "A")
        for ip in resultado:
            print (sub_alvo,"->",ip)
    except:
        pass
