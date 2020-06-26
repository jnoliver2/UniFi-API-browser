set interfaces ethernet eth0 duplex auto
set interfaces ethernet eth0 speed auto
set interfaces ethernet eth0 vif 181 address 175.175.177.2/24
set interfaces ethernet eth0 vif 181 description Internet
set interfaces ethernet eth1 description Local
set interfaces ethernet eth1 duplex auto
set interfaces ethernet eth1 speed auto
set interfaces ethernet eth2 description Local
set interfaces ethernet eth2 duplex auto
set interfaces ethernet eth2 speed auto
set interfaces ethernet eth3 description Local
set interfaces ethernet eth3 duplex auto
set interfaces ethernet eth3 speed auto
set interfaces ethernet eth4 description Local
set interfaces ethernet eth4 duplex auto
set interfaces ethernet eth4 speed auto
set interfaces ethernet eth5 duplex auto
set interfaces ethernet eth5 speed auto
set interfaces loopback lo
set interfaces switch switch0 address 10.0.154.2/24
set interfaces switch switch0 description Local
set interfaces switch switch0 mtu 1500
set interfaces switch switch0 switch-port interface eth1
set interfaces switch switch0 switch-port interface eth2
set interfaces switch switch0 switch-port interface eth3
set interfaces switch switch0 switch-port interface eth4
set interfaces switch switch0 switch-port vlan-aware disable
set service dns forwarding cache-size 150
set service dns forwarding listen-on LISTENONPORT
set service dns forwarding listen-on switch0
set service gui http-port 80
set service gui https-port 443
set service gui older-ciphers enable
set service nat rule 5010 description 'masquerade for WAN'
set service nat rule 5010 outbound-interface eth0.181
set service nat rule 5010 type masquerade
set service ssh port 22
set service ssh protocol-version v2
set system gateway-address 175.175.177.1
set system host-name ubnt
set system login user admin authentication encrypted-password '$6$SnYmI.9S$TIAN1RHw65cPzESBGWuSxR6pye30/Ea/DOa4R/U1QCDqEViNj4gc.8LZPB.WgRB0mTuyyay2djXxraiQahKRy1'
set system login user admin level admin
set system name-server 8.8.8.8
set system ntp server 0.ubnt.pool.ntp.org
set system ntp server 1.ubnt.pool.ntp.org
set system ntp server 2.ubnt.pool.ntp.org
set system ntp server 3.ubnt.pool.ntp.org
set system syslog global facility all level notice
set system syslog global facility protocols level debug
set system time-zone UTC