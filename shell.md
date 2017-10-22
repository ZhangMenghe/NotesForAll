# CSE 260 PUB<br>
export PUB=/share/class/public/cse260-fa17  # on bang <br>
export PUB=/share/public/cse260-fa17            # on sorken<br>
export PUB=/share/class/public/cse260-fa17 # on AWS EC2 (amazon)<br>

#sorken<br>
ssh user@sorken.ucsd.edu<br>

# bang
- Login to your account on the cluster's login server node (not the front end server node) by typing:
```sh
ssh YourADLogin@ccom-bang-login.ucsd.edu
```

# [Sun Grid Engine Reference](http://docs.oracle.com/cd/E19279-01/820-3257-12/n1ge.html#50577430_65574)

# Secure Copy (scp)
- Copy the file "foobar.txt" from a remote host to the local host
```sh
$ scp your_username@remotehost.edu:foobar.txt /some/local/directory
```
- Copy the file "foobar.txt" from the local host to a remote host
```sh
$ scp foobar.txt your_username@remotehost.edu:/some/remote/directory
```
- Copy the directory "foo" from the local host to a remote host's directory "bar"
```sh
$ scp -r foo your_username@remotehost.edu:/some/remote/directory/bar
```
- Copy the file "foobar.txt" from remote host "rh1.edu" to remote host "rh2.edu"
```sh
$ scp your_username@rh1.edu:/some/remote/directory/foobar.txt \
your_username@rh2.edu:/some/remote/directory/
```
- Copying the files "foo.txt" and "bar.txt" from the local host to your home directory on the remote host
```sh
$ scp foo.txt bar.txt your_username@remotehost.edu:~
```
- Copy the file "foobar.txt" from the local host to a remote host using port 2264
```sh
$ scp -P 2264 foobar.txt your_username@remotehost.edu:/some/remote/directory
```
- Copy multiple files from the remote host to your current directory on the local host
```sh
$ scp your_username@remotehost.edu:/some/remote/directory/\{a,b,c\} .
$ scp your_username@remotehost.edu:~/\{foo.txt,bar.txt\} 
```
