
# Minecraft
## サーバーの立て方(ubuntu)
```bash
sudo apt update
sudo apt upgrade

# サーバーが使用するJava Runtimeをインストールする
sudo apt install openjdk-17-jdk

# Minecraftサーバーが使用するポートを開ける。
sudo ufw allow 25556

# EULAに同意する。
sudo vi eula.txt
# 更新する
# eula=true

# サーバーを起動する。
sudo java -jar server.jar nogui

#IPを確認する。これを使って画面でIPアドレスを入力する。
ifconfig

kiyo@DrifterMiniPC:~$ ifconfig
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 172.27.242.135  netmask 255.255.240.0  broadcast 172.27.255.255
        inet6 fe80::215:5dff:fe89:31fa  prefixlen 64  scopeid 0x20<link>
        ether 00:15:5d:89:31:fa  txqueuelen 1000  (イーサネット)
        RX packets 444223  bytes 648982443 (648.9 MB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 34134  bytes 3353248 (3.3 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (ローカルループバック)
        RX packets 497191  bytes 124616497 (124.6 MB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 497191  bytes 124616497 (124.6 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```
## docker-composeで起動する。
```bash
docker-compose up -d
```
