# Windows 7+ users setup

If you're using Windows 7+ / Windows Server 2003+, setting up the project in the beginning gets a bit more tricky. But don't worry, this will be only in the beginning and we're here to guide you.

It is recommended to use Chocolatey to help you to install the required programs. Chocolatey is a software management solution similar to brew in Mac/Linux that installs programs with a simple command. You can download it using their instructions: https://chocolatey.org/docs/installation. After installation, you might need to restart your PowerShell window or Prompt commands (cmd). 

If you don't have the below programs already, you can download them using the line code in PowerShell or Prompt commands (cmd):
- Docker Toolbox: `choco install docker-toolbox`
- Make: `choco install make`
- Python3: `choco install python3`
- Git: `choco install git`

After the installation, you should restart the PowerShell window or Prompt commands (cmd) before you go to the next step.

You need to run `Docker Quickstart Terminal` so the virtual machine is created for the first time. After you see the whale there, you’ll be able to run `make setup`. So that's it! Now you need to go back to [README.md](README.md) and follow the instructions from there. 

**Notes**

1. If you use PowerShell to download Chocolatey, you will need PowerShell version 3+. To check your version, open PowerShell with a right-click and run as administrator. Then run `Get-Host | Select-Object Version`, this will give you the current version you're using. If you don't have version 3+, you can update it at https://www.microsoft.com/en-us/download/details.aspx?id=34595

2. Windows 10 users that meet [these requirements](https://docs.docker.com/docker-for-windows/install/#system-requirements) may be able to use Docker Desktop instead of Docker Toolbox but we haven't tested it and there is no documentation here for how to do it.