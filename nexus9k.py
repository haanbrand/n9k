import requests
import json


IP = '10.132.108.6'
ip_list = ['10.132.108.6','10.132.108.5']

url='http://' + IP + '/ins'
switchuser='cockburnj'
switchpassword='J@sonasd02'

myheaders={'content-type':'application/json'}
show_ver={
  "ins_api": {
    "version": "1.0",
    "type": "cli_show",
    "chunk": "0",
    "sid": "1",
    "input": "show version",
    "output_format": "json"
  }
}

show_inventory={
  "ins_api": {
    "version": "1.0",
    "type": "cli_show",
    "chunk": "0",
    "sid": "1",
    "input": "show invent",
    "output_format": "json"
  }
}

def showver(url):
	response = requests.post(url,data=json.dumps(show_ver), headers=myheaders,auth=(switchuser,switchpassword)).json()
	chassis_id = response['ins_api']['outputs']['output']['body']['chassis_id']
	host_name = response['ins_api']['outputs']['output']['body']['host_name']
	kickstart_ver_str = response['ins_api']['outputs']['output']['body']['kickstart_ver_str']
	return chassis_id, host_name, kickstart_ver_str
	
def showinventory(url):
	response = requests.post(url,data=json.dumps(show_inventory), headers=myheaders,auth=(switchuser,switchpassword)).json()
	items = response['ins_api']['outputs']['output']['body']['TABLE_inv']['ROW_inv']
	for item in items:
		name = item['name']
		desc = item['desc']
		productid = item['productid']
		serialnum = item['serialnum']
		print name
		print desc
		print productid
		print serialnum
		print '='*20

	
	
	
#================================MAIN STARTS================================================	



print 'Inventory...'
for ip in ip_list:
	IP = ip
	url='http://' + IP + '/ins'
	print 'Contacting device with URL: ' + url
	chassis_id, host_name, kickstart_ver_str = showver(url)	
	print chassis_id
	print host_name
	print kickstart_ver_str
	showinventory(url)

