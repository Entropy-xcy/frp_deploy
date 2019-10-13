wget https://github.com/fatedier/frp/releases/download/v0.28.0/frp_0.28.0_linux_amd64.tar.gz
tar xvf frp_0.28.0_linux_amd64.tar.gz
cp ./frp_0.28.0_linux_amd64/frpc ./
cp ./frp_0.28.0_linux_amd64/frps ./
rm -r ./frp_0.28.0_linux_amd64/
rm frp_0.28.0_linux_amd64.tar.gz
python3 client_ini_gen.py
sudo nohup ./frpc -c frpc0.ini > frpc0.log &
sudo nohup ./frpc -c frpc1.ini > frpc1.log &
sudo nohup ./frpc -c frpc2.ini > frpc2.log &
sudo nohup ./frpc -c frpc3.ini > frpc3.log &
sudo nohup ./frpc -c frpc4.ini > frpc4.log &
sudo nohup ./frpc -c frpc5.ini > frpc5.log &
sudo nohup ./frpc -c frpc6.ini > frpc6.log &
sudo nohup ./frpc -c frpc7.ini > frpc7.log &
sudo nohup ./frpc -c frpc8.ini > frpc8.log &
sudo nohup ./frpc -c frpc9.ini > frpc9.log &
sudo nohup ./frpc -c frpc10.ini > frpc10.log &
sudo nohup ./frpc -c frpc11.ini > frpc11.log &
sudo nohup ./frpc -c frpc12.ini > frpc12.log &
sudo nohup ./frpc -c frpc13.ini > frpc13.log &
sudo nohup ./frpc -c frpc14.ini > frpc14.log &
sudo nohup ./frpc -c frpc15.ini > frpc15.log &
sudo nohup ./frpc -c frpc16.ini > frpc16.log &
sudo nohup ./frpc -c frpc17.ini > frpc17.log &
sudo nohup ./frpc -c frpc18.ini > frpc18.log &
sudo nohup ./frpc -c frpc19.ini > frpc19.log &
sudo nohup ./frpc -c frpc20.ini > frpc20.log &
sudo nohup ./frpc -c frpc21.ini > frpc21.log &
sudo nohup ./frpc -c frpc22.ini > frpc22.log &
sudo nohup ./frpc -c frpc23.ini > frpc23.log &
sudo nohup ./frpc -c frpc24.ini > frpc24.log &
sudo nohup ./frpc -c frpc25.ini > frpc25.log &
sudo nohup ./frpc -c frpc26.ini > frpc26.log &
sudo nohup ./frpc -c frpc27.ini > frpc27.log &
sudo nohup ./frpc -c frpc28.ini > frpc28.log &
sudo nohup ./frpc -c frpc29.ini > frpc29.log &
