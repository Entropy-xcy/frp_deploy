#!/usr/bin/env bash
python3 client_ini_gen.py
nohup ./frpc -c frpc0.ini > frpc0.log &
nohup ./frpc -c frpc1.ini > frpc1.log &
nohup ./frpc -c frpc2.ini > frpc2.log &
nohup ./frpc -c frpc3.ini > frpc3.log &
nohup ./frpc -c frpc4.ini > frpc4.log &
nohup ./frpc -c frpc5.ini > frpc5.log &
nohup ./frpc -c frpc6.ini > frpc6.log &
nohup ./frpc -c frpc7.ini > frpc7.log &
nohup ./frpc -c frpc8.ini > frpc8.log &
nohup ./frpc -c frpc9.ini > frpc9.log &
tail -f /dev/null
