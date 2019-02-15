# RaspberryPi 3 B+

- [Raspberry Pi](https://www.raspberrypi.org/)
- [Raspberry Pi Documents](https://www.raspberrypi.org/documentation/)

##### The Raspberry Pi 3 Model B+ is the latest product in the Raspberry Pi 3 range.
>・Broadcom BCM2837B0, Cortex-A53 (ARMv8) 64-bit SoC @ 1.4GHz
>・1GB LPDDR2 SDRAM
>・2.4GHz and 5GHz IEEE 802.11.b/g/n/ac wireless LAN, Bluetooth 4.2, BLE
>・Gigabit Ethernet over USB 2.0 (maximum throughput 300 Mbps)
>・Extended 40-pin GPIO header
>・Full-size HDMI
>・4 USB 2.0 ports
>・CSI camera port for connecting a Raspberry Pi camera
>・DSI display port for connecting a Raspberry Pi touchscreen display
>・4-pole stereo output and composite video port
>・Micro SD port for loading your operating system and storing data
>・5V/2.5A DC power input
>・Power-over-Ethernet (PoE) support (requires separate PoE HAT)

## SDカード初期化
- [SDカードメモリフォーマッター](https://www.sdcard.org/jp/downloads/formatter_4/)

## OS
- [NOOBS](https://www.raspberrypi.org/downloads/noobs/)
- [Raspbian](https://www.raspberrypi.org/downloads/raspbian/)
- [Win10 IoT Core](https://go.microsoft.com/fwlink/?LinkId=846058)

## Image Writer

- [Etcher](https://www.balena.io/etcher/)

## Wi-Fi

- SSIDをステルスにしているので、GUIで設定が出来なかった。ことが発端。

### 無線LANルータの設定状況
- SSIDステルスを設定している
- 通信方法
 - 規格：WPA2
 - 暗号化：AES
 - 認証：事前共有鍵(PSK)

### まずは状態確認

```sh:iwconfig
$ iwconfig
```

```sh:iwlist
$ sudo iwlist wlan0 scan
```

```sh:ifconfig
$ ifconfig
```

```sh:パスワードを暗号化する
$ wpa_passphrase "ssid" "MyPassphrase"
```

```sh:wpa_supplicant.confファイルを編集する
$ sudo vi /etc/wpa_supplicant/wpa_supplicant.conf
```

```txt:/etc/wpa_supplicant/wpa_supplicant.conf
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=JP
network={
        ssid="ネットワーク識別子"
        scan_ssid=1
        psk="パスフレーズ"
}
```
※ 詳細は、[FreeBSD manual page](https://www.freebsd.org/cgi/man.cgi?query=wpa_supplicant.conf&sektion=5&apropos=0&manpath=NetBSD+6.1.5)

##### ※/etc/network/interfaces.d/配下に個別に設定ファイルを作るのがベター？(要検証)

```sh:interfacesファイルを編集する
$ sudo vi /etc/network/interfaces
```

##### DHCPの場合
```txt:/etc/network/interfaces
auto wlan0
iface wlan0 inet dhcp
wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf
```

##### IP固定の場合
```txt:/etc/network/interfaces
auto wlan0
iface wlan0 inet static
  address 192.168.0.200/24
  gateway 192.168.0.1
wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf
```

```sh:ファイルへのアクセス制御
$ sudo chmod 600 /etc/wpa_supplicant/wpa_supplicant.conf
$ sudo chmod 600 /etc/network/interfaces
```

---

## Raspberry Piへの入出力制御

- RasPiへの入出力は、[GPIO](https://www.raspberrypi.org/documentation/usage/gpio/README.md) (General-Purpose Input/Output：[多目的入出力](https://ja.wikipedia.org/wiki/GPIO))ポートを介して行う
- [RasPi3 B+ Pin配列](https://pinout.xyz/)

```sh:実機のPin確認
$ pinout
```

##### PWM (Pulse Width Modulation：[パルス幅変調](https://ja.wikipedia.org/wiki/%E3%83%91%E3%83%AB%E3%82%B9%E5%B9%85%E5%A4%89%E8%AA%BF))

##### SPI (Serial Peripheral Interface：[シリアル・ペリフェラル・インタフェース](https://ja.wikipedia.org/wiki/%E3%82%B7%E3%83%AA%E3%82%A2%E3%83%AB%E3%83%BB%E3%83%9A%E3%83%AA%E3%83%95%E3%82%A7%E3%83%A9%E3%83%AB%E3%83%BB%E3%82%A4%E3%83%B3%E3%82%BF%E3%83%95%E3%82%A7%E3%83%BC%E3%82%B9))

|制御信号|用途|
|:-:|:-:|
|SCK (Serial Clock)|同期クロック|
|MISO (Master In Slave Out)|入力|
|MOSI (Master Out Slave In)|出力|
|SS (Slave Select)|スレーブ識別|

##### I2C (Inter-Integrated Circuit：[アイ・スクエアド・シー](https://ja.wikipedia.org/wiki/I2C))

- SDA (Serial Data):
- SCL (Serial Clock):

## DIY電子工作
- [Fritzing (配線図作成ソフト)](http://fritzing.org/home/)

### 参考サイト
- [Fritzingの使い方](https://www.fabshop.jp/fritzing%E3%81%A7%E5%9B%9E%E8%B7%AF%E5%9B%B3%E3%83%BB%E9%85%8D%E7%B7%9A%E5%9B%B3%E3%82%92%E6%9B%B8%E3%81%84%E3%81%A6%E3%81%BF%E3%82%88%E3%81%86%EF%BC%81/)
- [無線LANの基本 - WiFi](http://manual.aptosid.com/ja/inet-wpa-ja.htm#wpa)
- [WiFi](https://sites.google.com/site/teyasn001/ubuntu-12-10/nettowaku-she-ding)
- [RasPi AP](http://kassyjp.ninja-web.net/ras/jessie/bridge.htm)
