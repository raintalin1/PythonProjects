import paramiko

# SSH connection details
ssh_host = ''
ssh_port = 0  # Default SSH port is 22
ssh_username = ''
ssh_password = ''

class sshConncetionPassCommands:
    def __init__(self, host, port, username, password, commands):
        host = host
        port = port
        username = username
        password = password
        commands = commands

    def commandInPassOut(host, port, username, password, commands, outIndex=-1):

        ssh_host = host
        ssh_port = port
        ssh_username = username
        ssh_password = password
        try:
            ssh_client = paramiko.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            ssh_client.connect(ssh_host, port=ssh_port, username=ssh_username, password=ssh_password)
            stdin, stdout, stderr = ssh_client.exec_command(commands)

            output = stdout.read().decode('utf-8').splitlines()
            password = output[outIndex]

            ssh_client.close()
            print(output, password)
            return password

        except paramiko.AuthenticationException:
            print("Authentication failed. Please check your credentials.")
        except paramiko.SSHException as e:
            print("SSH connection failed:", str(e))
        except Exception as e:
            print("An error occurred:", str(e))
