killall frpc
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

