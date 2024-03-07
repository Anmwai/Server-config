from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
import paramiko

def server_output(request):
    # SSH connection details
    hostname = '151.80.64.159'
    password = 'JQ7uvHWuDd'
    command = 'uptime'  # Command to execute
    
    # Establish SSH connection
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname, username='ubuntu', password='JQ7uvHWuDd')
    
    # Execute command
    stdin, stdout, stderr = ssh.exec_command(command)
    
    # Read output
    output = stdout.read().decode()
    
    # Close SSH connection
    ssh.close()
    
    # Return the output as JSON
    return JsonResponse({'output': output})
