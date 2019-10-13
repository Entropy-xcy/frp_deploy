wget https://github.com/fatedier/frp/releases/download/v0.28.0/frp_0.28.0_linux_amd64.tar.gz
tar xvf frp_0.28.0_linux_amd64.tar.gz
cp ./frp_0.28.0_linux_amd64/frpc ./
cp ./frp_0.28.0_linux_amd64/frps ./
rm -r ./frp_0.28.0_linux_amd64/
rm frp_0.28.0_linux_amd64.tar.gz
python3 server_ini_gen.py
ulimit -n 65535
sudo nohup ./frps -c frps0.ini > frps0.log &
sudo nohup ./frps -c frps1.ini > frps1.log &
sudo nohup ./frps -c frps2.ini > frps2.log &
sudo nohup ./frps -c frps3.ini > frps3.log &
sudo nohup ./frps -c frps4.ini > frps4.log &
sudo nohup ./frps -c frps5.ini > frps5.log &
sudo nohup ./frps -c frps6.ini > frps6.log &
sudo nohup ./frps -c frps7.ini > frps7.log &
sudo nohup ./frps -c frps8.ini > frps8.log &
sudo nohup ./frps -c frps9.ini > frps9.log &
sudo nohup ./frps -c frps10.ini > frps10.log &
sudo nohup ./frps -c frps11.ini > frps11.log &
sudo nohup ./frps -c frps12.ini > frps12.log &
sudo nohup ./frps -c frps13.ini > frps13.log &
sudo nohup ./frps -c frps14.ini > frps14.log &
sudo nohup ./frps -c frps15.ini > frps15.log &
sudo nohup ./frps -c frps16.ini > frps16.log &
sudo nohup ./frps -c frps17.ini > frps17.log &
sudo nohup ./frps -c frps18.ini > frps18.log &
sudo nohup ./frps -c frps19.ini > frps19.log &
sudo nohup ./frps -c frps20.ini > frps20.log &
sudo nohup ./frps -c frps21.ini > frps21.log &
sudo nohup ./frps -c frps22.ini > frps22.log &
sudo nohup ./frps -c frps23.ini > frps23.log &
sudo nohup ./frps -c frps24.ini > frps24.log &
sudo nohup ./frps -c frps25.ini > frps25.log &
sudo nohup ./frps -c frps26.ini > frps26.log &
sudo nohup ./frps -c frps27.ini > frps27.log &
sudo nohup ./frps -c frps28.ini > frps28.log &
sudo nohup ./frps -c frps29.ini > frps29.log &