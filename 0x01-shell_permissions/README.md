# 0x01. Shell, permissions

```
0-iam_betty 			// changes your user ID to betty
1-who_am_i 			// prints the effective userid of the current user
4-empty 			// creates an empty file called `hello`
2-groups 			// prints all the groups the current user is part of
3-new_owner 			// changes the owner of the file `hello` to the user `betty`
5-execute 			// adds execute permission to the owner of the file `hello`
6-multiple_permissions  	// adds x permission to owner and group owner, and r permission to other users, to the file `hello`
7-everybody 			// adds execution permission to the owner, the group owner and the other users, to the file `hello` (without commas)
8-James_Bond 			// sets the permission to the file hello as follows: u - 0, g - 0, o - 7
9-John_Doe 			// sets the mode of the file hello to -rwxr-x-wx
10-mirror_permissions 		// sets the mode of the file `hello` the same as `olleh’s` mode (files in a workdir)
11-directories_permissions 	// adds x permission to all subdirectories for everyone without affecting the files
12-directory_permissions 	// creates a directory called dir_holberton with permissions 751 in the workdir
13-change_group 		// changes the group owner to `holberton` for the file `hello`
14-change_owner_and_group 	// changes owner to `betty` and group owner to `holberton` for all files and directories in the workdir
15-symbolic_link_permissions 	// changes the owner and the group owner of the file `_hello` (symbolic link) to betty:holberton 
16-if_only 			// changes the owner of the file `hello` to `betty` only if it is owned by the user `guillaume`
100-Star_Wars 			// plays the StarWars IV episode in terminal
101-man_holberton 		// man that looks exactly like [this](//s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/207/man_holberton.PNG) (advanced project)
```
