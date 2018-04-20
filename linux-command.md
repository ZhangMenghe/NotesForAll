# Windows Ubuntu
* Change Password<br>
1. In cmd prompt : 
`ubuntu config --default-user root`<br>
2. Now Bash on Ubuntu on Windows logs you in as root without asking password, use<br>
`passwd your_username`<br>
3. Change the default user back to your normal user in Windows command prompt <br>
`ubuntu config --default-user  your_username`

* Ubuntu commend CheetSheet
1. copy Directory<br>
`cp -r <srcDir> <dstDir>`
`-r` means recursively, copy subdirecotires as well.
2. Current Dir `pwd`
3. What files the package contains<br>
 `dpkg -L <packagename>`

# How to install virtualenv:

### Install **pip** first

    sudo apt-get install python3-pip

### Then install **virtualenv** using pip3

    sudo pip3 install virtualenv 

### Now create a virtual environment 

    virtualenv venv 

>you can use any name insted of **venv**

### You can also use a Python interpreter of your choice

    virtualenv -p /usr/bin/python2.7 venv
  
### Active your virtual environment:    
    
    source venv/bin/activate
    
### Using fish shell:    
    
    source venv/bin/activate.fish

### To deactivate:

    deactivate

### Create virtualenv using Python3
    virtualenv -p python3 myenv

### Instead of using virtualenv you can use this command in Python3
    python3 -m venv myenv

### Install package in virtual env
    
    pip install <...>

### If have to use apt-get 

    sudo apt-get install python-pycurl
    cp /usr/lib/python2.7/dist-packages/pycurl* ~/.virtualenvs/myenv/lib/python2.7/site-packages/
