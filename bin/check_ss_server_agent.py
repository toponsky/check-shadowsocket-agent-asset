import subprocess,os,json,socket
from dateutil.parser import parse

def is_date(string, fuzzy=False):
    """
    Return whether the string can be interpreted as a date.

    :param string: str, string to check for date
    :param fuzzy: bool, ignore unknown tokens in string if True
    """
    try: 
        parse(string, fuzzy=fuzzy)
        return True

    except ValueError:
        return False

def get_ip_address():
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  s.connect(("8.8.8.8", 80))
  ip = s.getsockname()[0]
  s.close()
  return ip

def get_error_msg():
  data = {}
  data['subject'] = 'Check SS Server'
  data['body'] = "Did not detect SS Server task for tenant with IP :" + get_ip_address()
  return json.dumps(data)

def check_ss_server_task():
    p = subprocess.Popen("docker container list", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    output = p.communicate()[0].decode("utf-8")
    
    if(output.split("\n")[1].find("ss_server") != -1):
        print(output)
        exit(0)
    else:
        print(get_error_msg())
        exit(2)


check_ss_server_task()