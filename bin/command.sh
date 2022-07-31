
#!/bin/sh
scriptDir="$(dirname $(dirname $(realpath $0)) )/bin"
/usr/bin/python "$scriptDir/check_ss_server_agent.py"