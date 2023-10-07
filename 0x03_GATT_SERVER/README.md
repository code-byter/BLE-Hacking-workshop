# Creating a GATT server with Blesss
Make sure bless is installed. 

## Interacting with the target
1. We can use nrfconnect app (Not reliable for writing according to my own tests)

2. Use hcitool or other GATT client

```bash
#Identify the target device

hcitool lescan
...
E4:5F:01:EC:3A:7D Basic GATT server hwh_
...

pi@pi2:~ $ gatttool  -b E4:5F:01:EC:3A:7D -I
[E4:5F:01:EC:3A:7D][LE]> connect
Attempting to connect to E4:5F:01:EC:3A:7D
Connection successful
[E4:5F:01:EC:3A:7D][LE]> characteristics 
handle: 0x0002, char properties: 0x02, char value handle: 0x0003, uuid: 00002a00-0000-1000-8000-00805f9b34fb
[...]
handle: 0x0049, char properties: 0x0a, char value handle: 0x004a, uuid: abcf9298-6d32-4615-a365-61f074114425

411442501:EC:3A:7D][LE]> char-read-uuid abcf9298-6d32-4615-a365-61f074114425
handle: 0x004a 	 value: 61 20 72 61 6e 64 6f 6d 63 68 61 72 

[E4:5F:01:EC:3A:7D][LE]> char-write-
char-write-cmd  char-write-req  

[E4:5F:01:EC:3A:7D][LE]> char-write-cmd 
Usage: char-write-cmd <handle> <new value>          

[E4:5F:01:EC:3A:7D][LE]> char-write-cmd abcf9298-6d32-4615-a365-61f074114425 "EST"
```

After the above sequence is executed see the logs of your `gat_server_bless.py`