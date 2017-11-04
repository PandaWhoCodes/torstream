import os


def test_system():
    """Runs few tests to check if npm and peerflix is installed on the system."""
    if os.system('npm --version') != 0:
        print('NPM not installed installed, please read the Readme file for more information.')
        exit()
    if os.system('peerflix --version') != 0:
        print('Peerflix not installed, installing..')
        os.system('npm install -g peerflix')
