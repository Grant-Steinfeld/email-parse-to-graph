# email-parse-to-graph
subscription email parser


### Use Postfix to receive emails to your server

```bash

sudo su

#copy just in case
cp /etc/aliases /etc/aliases.1

```

Add following line to bottom of file

```sh
weather:   "|/home/developer/newdev/breakingnews weather"
```

This line will allow mail to weather@<your domain> to be piped to the program ( shell script ) in this case `breakingnews`
  with a parameter `weather`
  
  
