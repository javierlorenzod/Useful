## Set up Jupyter Notebook on remote server

This useful how to is based on [this article][1]:

1. In the remote machine, start jupyter notebook without browser in your chosen port:
```bash
jupyter notebook --no-browser --port=[XXXX]
```
1. In your local machine, create an SSH tunnel to bind the remote port to one of your local ports:

     - USER: user name
     - SERVER: IP address of server (public or private if you are using VPN)
     - YYYY: Local port that you want to use for the binding
     - XXXX: Remote port in which the notebook is settled
     
```
ssh -f [USER]@[SERVER] -L [YYYY]:localhost:[XXXX] -N
```

1. now you can connect to the notebook accessing in your browser to `localhost:YYYY`

1. When you are done, kill the tunnel if you don't want to keep it in your current session (more info in [this post][2]).
```
ps aux | grep ssh # Find the process and annotate the PID
kill PID
```


[1]: https://coderwall.com/p/y1rwfw/jupyter-notebook-on-remote-server
[2]: https://superuser.com/questions/87014/how-do-i-remove-an-ssh-forwarded-port
