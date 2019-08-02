wget https://github.com/fatedier/frp/releases/download/v0.28.0/frp_0.28.0_linux_amd64.tar.gz
tar xvf frp_0.28.0_linux_amd64.tar.gz
cp ./frp_0.28.0_linux_amd64/frpc ./
cp ./frp_0.28.0_linux_amd64/frps ./
rm -r ./frp_0.28.0_linux_amd64/
rm frp_0.28.0_linux_amd64.tar.gz
python3 server_ini_gen.py
sudo nohup ./frps -c frps0.ini > frps0.ini.log &
sudo nohup ./frps -c frps1.ini > frps1.ini.log &
sudo nohup ./frps -c frps2.ini > frps2.ini.log &
sudo nohup ./frps -c frps3.ini > frps3.ini.log &
sudo nohup ./frps -c frps4.ini > frps4.ini.log &
sudo nohup ./frps -c frps5.ini > frps5.ini.log &
sudo nohup ./frps -c frps6.ini > frps6.ini.log &
sudo nohup ./frps -c frps7.ini > frps7.ini.log &
sudo nohup ./frps -c frps8.ini > frps8.ini.log &
sudo nohup ./frps -c frps9.ini > frps9.ini.log &
