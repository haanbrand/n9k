import requests
import json


#ip_list = ['10.132.108.6','10.132.108.7','10.132.108.8','10.132.108.9','10.132.108.12','10.132.108.13','10.132.108.14','10.132.108.15']
ip_list = ['10.132.108.7']
switchuser='cockburnj'
switchpassword='J@sonasd02'
myheaders={'content-type':'application/json'}


intf_status={
  "ins_api": {
    "version": "1.0",
    "type": "cli_show",
    "chunk": "0",
    "sid": "1",
    "input": "show interface status",
    "output_format": "json"
  }
}

def get_port_info(IP):
	url='http://' + IP + '/ins'
	response = requests.post(url,data=json.dumps(intf_status), headers=myheaders,auth=(switchuser,switchpassword)).json()
	port_info = response['ins_api']['outputs']['output']['body']['TABLE_interface']['ROW_interface']
	#print port_info
	for port in port_info:
		#print port
		interface = str(port['interface'])
		intf_state = str(port['state'])
		#checks only Ethernet interfaces, not mgmt etc...
		if "Ethernet1" in interface and int(interface.split('/')[1]) < 46:
			#creates list that looks like ['Ethernet1', '48']
			intf = interface
			int_nr_list = interface.split('/')
			try:
				intf_name = port['name']
			except:
				intf_name = '**check port**'
			intf_vlan = str(port['vlan'])
			print interface.split('/')[1]
			print intf + ' ' + intf_state + ' ' + intf_name + ' ' + intf_vlan
			
		else:
			print 'Skipping ' + str(interface)
			continue
			
'''
TODO
1. Get configured info on switch interfaces - DONE
2. Check Connected
3. Get intf description for hostname attached
4. Get IP and ARP info for hostname
5. Compare configured and actual data
6. Print report
'''


#===========================MAIN PROG START===============================================


print 'Starting...'
report = open('interface_report.txt','w')

for IP in ip_list:
	print 'Checking device with IP: ' + IP
	get_port_info(IP)
	
report.close()

