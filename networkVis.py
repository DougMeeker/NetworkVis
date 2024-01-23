import json
from pyvis.network import Network

network_name = "50_330"
net = Network(height="960px", select_menu=True)


with open(network_name+ ".json", "r") as file:
    data = json.load(file)

    for host in data:
        for host_ip in host.keys():
            net.add_node(host_ip, label=host_ip)
            for interface in host[host_ip].keys():
                print (host[host_ip][interface][0])
                guest_ip = host[host_ip][interface][0]['ip']
                guest_port = host[host_ip][interface][0]['port']
                guest_hostname = host[host_ip][interface][0]['host']
                net.add_node(guest_ip, label=guest_ip, title= guest_hostname + " local port: " + guest_port )
                net.add_edge(host_ip, guest_ip)  


net.show(network_name + ".html", notebook=False)
