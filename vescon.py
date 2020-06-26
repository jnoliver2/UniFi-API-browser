set firewall group network-group PRIVATE_NETS network 192.168.0.0/16
set firewall group network-group PRIVATE_NETS network 172.16.0.0/12
set firewall group network-group PRIVATE_NETS network 10.0.0.0/8
set firewall group port-group mails description ''
set firewall group port-group mails port 25
set firewall group port-group mails port 143
set firewall group port-group mails port 587
set firewall group port-group mails port 465
set firewall ipv6-receive-redirects disable
set firewall ipv6-src-route disable
set firewall ip-src-route disable
set firewall log-martians disable
set firewall modify balance rule 10 action modify
set firewall modify balance rule 10 description 'do NOT load balance lan to lan'
set firewall modify balance rule 10 destination group network-group PRIVATE_NETS
set firewall modify balance rule 10 modify table main
set firewall modify balance rule 20 action modify
set firewall modify balance rule 20 description 'do NOT load balance destination public address'
set firewall modify balance rule 20 destination group address-group ADDRv4_eth0
set firewall modify balance rule 20 modify table main
set firewall modify balance rule 30 action modify
set firewall modify balance rule 30 description 'do NOT load balance destination public address'
set firewall modify balance rule 30 destination group address-group ADDRv4_eth1
set firewall modify balance rule 30 modify table main
set firewall modify balance rule 40 action modify
set firewall modify balance rule 40 description 'do NOT load balance destination public address'
set firewall modify balance rule 40 destination group address-group ADDRv4_eth2
set firewall modify balance rule 40 modify table main
set firewall modify balance rule 41 action modify
set firewall modify balance rule 41 description 'do NOT load balance destination public address'
set firewall modify balance rule 41 destination group address-group ADDRv4_eth3
set firewall modify balance rule 41 modify table main
set firewall modify balance rule 42 action modify
set firewall modify balance rule 42 description 'do NOT load balance destination public address'
set firewall modify balance rule 42 destination group address-group ADDRv4_eth4
set firewall modify balance rule 42 modify table main
set firewall modify balance rule 45 action modify
set firewall modify balance rule 45 modify lb-group ZK
set firewall modify balance rule 56 action modify
set firewall modify balance rule 56 destination group address-group ZUKU
set firewall modify balance rule 56 modify lb-group ZK
set firewall modify balance rule 80 action modify
set firewall modify balance rule 80 modify lb-group G
set firewall name Suspension default-action accept
set firewall name Suspension description ''
set firewall name Suspension rule 1 action drop
set firewall name Suspension rule 1 description drop_suspended
set firewall name Suspension rule 1 log disable
set firewall name Suspension rule 1 protocol all
set firewall name Suspension rule 1 source group address-group BLOCKED_USERS
set firewall name Suspension rule 1 state established enable
set firewall name Suspension rule 1 state invalid enable
set firewall name Suspension rule 1 state new enable
set firewall name Suspension rule 1 state related enable
set firewall name Suspension rule 2 action accept
set firewall name Suspension rule 2 description monitor_mails
set firewall name Suspension rule 2 destination group port-group mails
set firewall name Suspension rule 2 log enable
set firewall name Suspension rule 2 protocol all
set firewall receive-redirects disable
set firewall send-redirects enable
set firewall source-validation disable
set firewall syn-cookies enable
set interfaces ethernet eth0 address 192.168.110.2/24
set interfaces ethernet eth0 description ZK859316
set interfaces ethernet eth0 duplex auto
set interfaces ethernet eth0 poe output off
set interfaces ethernet eth0 speed auto
set interfaces ethernet eth1 address 192.168.100.5/24
set interfaces ethernet eth1 description Nyali-Uplink
set interfaces ethernet eth1 disable
set interfaces ethernet eth1 duplex auto
set interfaces ethernet eth1 poe output off
set interfaces ethernet eth1 speed auto
set interfaces ethernet eth2 address 192.168.120.2/24
set interfaces ethernet eth2 description 'ZK 919243 faith'
set interfaces ethernet eth2 duplex auto
set interfaces ethernet eth2 poe output off
set interfaces ethernet eth2 speed auto
set interfaces ethernet eth3 address 192.168.130.2/24
set interfaces ethernet eth3 description 'ZK 926305 Susan'
set interfaces ethernet eth3 duplex auto
set interfaces ethernet eth3 poe output off
set interfaces ethernet eth3 speed auto
set interfaces ethernet eth4 address 192.168.6.3/24
set interfaces ethernet eth4 description 'ZK Salim 220241'
set interfaces ethernet eth4 duplex auto
set interfaces ethernet eth4 speed auto
set interfaces ethernet eth5 duplex auto
set interfaces ethernet eth5 speed auto
set interfaces loopback lo
set interfaces switch switch0 address 10.0.154.2/24
set interfaces switch switch0 description Local
set interfaces switch switch0 firewall in modify balance
set interfaces switch switch0 firewall in name Suspension
set interfaces switch switch0 mtu 1500
set interfaces switch switch0 switch-port interface eth5
set interfaces switch switch0 switch-port vlan-aware disable
set load-balance group G interface eth0
set load-balance group G interface eth1 failover-only
set load-balance group G interface eth2
set load-balance group G interface eth3
set load-balance group G interface eth4
set load-balance group G lb-local enable
set load-balance group G lb-local-metric-change enable
set load-balance group GOOGLE interface eth0 failover-only
set load-balance group GOOGLE interface eth1 route-test initial-delay 60
set load-balance group GOOGLE interface eth1 route-test interval 10
set load-balance group GOOGLE interface eth1 route-test type ping target 10.0.154.1
set load-balance group GOOGLE lb-local enable
set load-balance group GOOGLE lb-local-metric-change enable
set load-balance group GOOGLE transition-script /config/scripts/clearcon
set load-balance group ZK interface eth0
set load-balance group ZK interface eth1 failover-only
set load-balance group ZK interface eth2
set load-balance group ZK interface eth3
set load-balance group ZK interface eth4
set load-balance group ZK lb-local enable
set load-balance group ZK lb-local-metric-change enable
set load-balance group ZK transition-script /config/scripts/clearcon
set port-forward auto-firewall enable
set port-forward hairpin-nat enable
set port-forward lan-interface switch0
set port-forward rule 1 description Willie
set port-forward rule 1 forward-to address 10.0.154.102
set port-forward rule 1 forward-to port 810-819
set port-forward rule 1 original-port 810-819
set port-forward rule 1 protocol tcp_udp
set port-forward rule 2 description Willie
set port-forward rule 2 forward-to address 10.0.154.102
set port-forward rule 2 forward-to port 22
set port-forward rule 2 original-port 820
set port-forward rule 2 protocol tcp_udp
set port-forward rule 3 description Willie
set port-forward rule 3 forward-to address 10.0.154.102
set port-forward rule 3 forward-to port 443
set port-forward rule 3 original-port 821
set port-forward rule 3 protocol tcp_udp
set port-forward rule 4 description 'Core S'
set port-forward rule 4 forward-to address 10.0.154.25
set port-forward rule 4 forward-to port 443
set port-forward rule 4 original-port 1000
set port-forward rule 4 protocol tcp_udp
set port-forward wan-interface eth0
set protocols static route 0.0.0.0/0 next-hop 192.168.6.1
set protocols static route 0.0.0.0/0 next-hop 192.168.100.1
set protocols static route 0.0.0.0/0 next-hop 192.168.110.1
set protocols static route 0.0.0.0/0 next-hop 192.168.120.1
set protocols static route 0.0.0.0/0 next-hop 192.168.130.1
set protocols static table 100 route 0.0.0.0/0 next-hop 192.168.110.1
set protocols static table 101 route 0.0.0.0/0 next-hop 192.168.100.1
set protocols static table 102 route 0.0.0.0/0 next-hop 192.168.120.1
set protocols static table 103 route 0.0.0.0/0 next-hop 192.168.130.1
set service dns forwarding cache-size 150
set service dns forwarding listen-on switch0
set service gui http-port 80
set service gui https-port 443
set service gui older-ciphers enable
set service nat rule 5000 description 'masquerade for WAN'
set service nat rule 5000 outbound-interface eth0
set service nat rule 5000 type masquerade
set service nat rule 5002 description 'masquerade for WAN 2'
set service nat rule 5002 outbound-interface eth1
set service nat rule 5002 type masquerade
set service nat rule 5004 description 'masquerade for WAN 3'
set service nat rule 5004 outbound-interface eth2
set service nat rule 5004 type masquerade
set service nat rule 5005 description 'masquerade for WAN 4'
set service nat rule 5005 outbound-interface eth3
set service nat rule 5005 type masquerade
set service nat rule 5006 description 'masquerade for WAN 5'
set service nat rule 5006 outbound-interface eth4
set service nat rule 5006 type masquerade
set service ssh port 22
set service ssh protocol-version v2
set service unms connection 'wss://10.0.154.3:9443+yxMisWg-cWIrk9SB_1rPBiozUEvqBeuFYrlkRkU0BC0AAAAA+allowUntrustedCertificate'
set system conntrack expect-table-size 4096
set system conntrack hash-size 4096
set system conntrack table-size 32768
set system conntrack tcp half-open-connections 512
set system conntrack tcp loose enable
set system conntrack tcp max-retrans 3
set system host-name Bamburi-Gateway
set system login user admin authentication encrypted-password '$6$dyvXhTwWkFg$NabfWfRohnHU7..1A5Dtq0L5zrgPvKXQ1G4E5VBSwez9amcaGOIxZ3Tp4coh4hhGgBXO28P1UK3jJNj1ojTwX.'
set system login user admin level admin
set system name-server 8.8.8.8
set system syslog global facility all level notice
set system syslog global facility protocols level debug
set system syslog host 'logs3.papertrailapp.com:34303' facility all level debug
set system time-zone Africa/Nairobi
set traffic-control advanced-queue queue-type fq-codel UCRM_FQ_CODEL
set traffic-control advanced-queue root queue 32767 attach-to global
set traffic-control advanced-queue root queue 32767 bandwidth 1000mbit
set traffic-control advanced-queue root queue 32767 description UCRM
