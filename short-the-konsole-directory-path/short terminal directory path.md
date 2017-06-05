here i am writing a method / way to shorten the directory path in the linux terminal / konsole to more compact one.
here instead of showing the whole directory path as  "<user name>@/Document/folder1/folder2/folder3/folder4"  this code will show 
 it into as current user working directory as "<user name>:folder4"

step to achive this is:


1. open the terminal in your ubuntu system .
2.  now run the command:
                            gedit  ~/.bashrc
3. now go to the end of the file 
4. now write the following there   
    
	      PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u\[\033[00m\]:\[\033[01;34m\]\W\[\033[00m\]\$ '
          
5. save the file and exit the editor
6. now after saving the file and exiting the editor ,run the following command
 
           source ~/.bashrc
7. it's completed .
    
now you can enjoy the experience on working on terminal / konsole.
		  
                          
by prashant rana
