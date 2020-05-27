

!/data/data/com.termux/files/usr/bin/bash

#TOOL: DARK FB
#Language: Bash
#Author: Termux ID

clear
echo "--SELAMAT DATANG DI PROGRAM SAYA--"
echo "-Semoga hari anda menyenangkan-]"
echo "--++[PROGRAM BY TRAINING08]+--"

echo "-Silahkan Pilih Menu yang diinginkan]-"

echo "1] Hack Akun Teman.."
echo "2] Hack Dari Grup.."

read -p"?] Silahkan masukkan pilhan anda [1-2]:" pilih

case $pilih in

1)
echo "[*] Akan Kami Hack Sabar napa
Tunggu.."
sleep 5
/system/bin/hackakuntemen -p

;;
2)
echo "*]  Akan Kami Hack Sabar Napa
Tunggu..
sleep 5
/system/bin/hackakungrup
;;
*)
echo "*] Anda Salah memasukkan pilihan silahkan
ulangi lagi dari awal..
sleep2
source$0

;;
esac
