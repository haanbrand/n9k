import requests
import json


#ip_list = ['10.132.108.4','10.132.108.5','10.132.108.6','10.132.108.7','10.132.108.8','10.132.108.9','10.132.108.10','10.132.108.11','10.132.108.12','10.132.108.13','10.132.108.14','10.132.108.15']
#ip_list = ['10.132.108.6']
ip_list = ['10.132.108.6','10.132.108.7','10.132.108.8','10.132.108.9','10.132.108.12','10.132.108.13','10.132.108.14','10.132.108.15']
switchuser='cockburnj'
switchpassword='J@sonasd02'

myheaders={'content-type':'application/json'}
show_cdp={
  "ins_api": {
    "version": "1.0",
    "type": "cli_show",
    "chunk": "0",
    "sid": "1",
    "input": "sh cdp nei",
    "output_format": "json"
  }
}

show_cdp_nei_det={
  "ins_api": {
    "version": "1.0",
    "type": "cli_show",
    "chunk": "0",
    "sid": "1",
    "input": "sh cdp nei det",
    "output_format": "json"
  }
}
#response = requests.post(url,data=json.dumps(show_cdp_nei_det), headers=myheaders,auth=(switchuser,switchpassword)).json()

show_hostname={
  "ins_api": {
    "version": "1.0",
    "type": "cli_show",
    "chunk": "0",
    "sid": "1",
    "input": "sh hostname",
    "output_format": "json"
  }
}



def get_cdp(IP):
	url='http://' + IP + '/ins'
	
	response = requests.post(url,data=json.dumps(show_cdp), headers=myheaders,auth=(switchuser,switchpassword)).json()
	neighbor_count = response['ins_api']['outputs']['output']['body']['neigh_count']
	neighbors = response['ins_api']['outputs']['output']['body']['TABLE_cdp_neighbor_brief_info']['ROW_cdp_neighbor_brief_info']
	
	response_sh_host = requests.post(url,data=json.dumps(show_hostname), headers=myheaders,auth=(switchuser,switchpassword)).json()
	hostname = response_sh_host['ins_api']['outputs']['output']['body']['hostname']
	
	for neighbor in neighbors:
		device_id = neighbor['device_id']
		local_intf = str(neighbor['intf_id'])
		#platform_id = str(neighbor['platform_id'])
		rem_intf = str(neighbor['port_id'])
		#print neighbor + ' ' + device_id + ' ' + local_intf + ' ' + platform_id + ' ' + rem_intf
		print hostname + ':' + local_intf + ' to ' + device_id + ' ' + rem_intf
		report.write(hostname + ':' + local_intf + ' to ' + device_id + ' ' + rem_intf + '\n')
	report.write('=' * 80 + '\n')
		
		

#===========================MAIN PROG START===============================================

print 'Starting...'
report = open('cdp_table.txt','w')

for IP in ip_list:
	print 'Contacting device with IP: ' + IP
	get_cdp(IP)
	
report.close()
	
