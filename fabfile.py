from fabric.operations import put, sudo, get, local

def install_fabric():
	"""
	This function install fabric on Ubuntu OS
	"""
	sudo('apt-get -y -q install python-pip gcc python-dev autoconf')
	sudo('pip install fabric')

