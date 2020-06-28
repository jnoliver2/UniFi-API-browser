set firewall all-ping enable
set firewall broadcast-ping disable
set firewall group address-group GOOGLE description ''
set firewall group network-group PRIVATE_NETS network 192.168.0.0/16
set firewall group network-group PRIVATE_NETS network 172.16.0.0/12
set firewall group network-group PRIVATE_NETS network 10.0.0.0/8
set firewall ipv6-receive-redirects disable
set firewall ipv6-src-route disable
set firewall ip-src-route disable
set firewall log-martians disable
set firewall modify balance
set firewall receive-redirects disable
set firewall send-redirects enable
set firewall source-validation disable
set firewall syn-cookies enable
set interfaces ethernet eth0 address 192.168.110.2/24
set interfaces ethernet eth0 description WAN
set interfaces ethernet eth0 duplex auto
set interfaces ethernet eth0 speed auto
set interfaces ethernet eth1 address 192.168.100.5/24
set interfaces ethernet eth1 description 'WAN 2'
set interfaces ethernet eth1 duplex auto
set interfaces ethernet eth1 speed auto
set interfaces ethernet eth2 address 192.168.120.2/24
set interfaces ethernet eth2 description 'WAN 3'
set interfaces ethernet eth2 duplex auto
set interfaces ethernet eth2 speed auto
set interfaces ethernet eth3 address 192.168.130.2/24
set interfaces ethernet eth3 description 'WAN 4'
set interfaces ethernet eth3 duplex auto
set interfaces ethernet eth3 speed auto
set interfaces ethernet eth3 vif 181 address 175.175.177.2/24
set interfaces ethernet eth3 vif 181 description DAPA
set interfaces ethernet eth3 vif 181 mtu 1500
set interfaces ethernet eth4 duplex auto
set interfaces ethernet eth4 poe output off
set interfaces ethernet eth4 speed auto
set interfaces loopback lo
set interfaces switch switch0 address 10.0.154.2/24
set interfaces switch switch0 description Local
set interfaces switch switch0 firewall in modify balance
set interfaces switch switch0 mtu 1500
set interfaces switch switch0 switch-port interface eth4
set interfaces switch switch0 switch-port vlan-aware disable
set load-balance group G exclude-local-dns disable
set load-balance group G flush-on-active enable
set load-balance group G gateway-update-interval 20
set load-balance group G interface eth0
set load-balance group G interface eth1 failover-only
set load-balance group G interface eth2
set load-balance group G interface eth3
set load-balance group G lb-local enable
set load-balance group G lb-local-metric-change disable
set load-balance group GOOGLE exclude-local-dns disable
set load-balance group GOOGLE flush-on-active enable
set load-balance group GOOGLE gateway-update-interval 20
set load-balance group GOOGLE interface eth1
set load-balance group GOOGLE interface eth3 failover-only
set load-balance group GOOGLE lb-local enable
set load-balance group GOOGLE lb-local-metric-change disable
set policy prefix-list PREFIX-FILTER rule 10 action deny
set policy prefix-list PREFIX-FILTER rule 10 le 32
set policy prefix-list PREFIX-FILTER rule 10 prefix 62.8.0.0/16
set policy prefix-list PREFIX-FILTER rule 1000 action permit
set policy prefix-list PREFIX-FILTER rule 1000 le 24
set policy prefix-list PREFIX-FILTER rule 1000 prefix 0.0.0.0/0
set policy route-map PREFIX-FILTER-MAP rule 10 action permit
set policy route-map PREFIX-FILTER-MAP rule 10 match ip address prefix-list PREFIX-FILTER
set protocols bgp 65530 neighbor 175.175.177.1 remote-as 65530
set protocols bgp 65530 neighbor 175.175.177.1 route-map import PREFIX-FILTER-MAP
set protocols bgp 65530 parameters router-id 175.175.177.2
set protocols static route 0.0.0.0/0 next-hop 192.168.100.1
set protocols static route 0.0.0.0/0 next-hop 192.168.110.1
set protocols static route 0.0.0.0/0 next-hop 192.168.120.1
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
set service nat rule 5006 description 'masquerade for WAN 4'
set service nat rule 5006 outbound-interface eth3
set service nat rule 5006 type masquerade
set service nat rule 5007 description 'masquerade for WAN DAPA'
set service nat rule 5007 log disable
set service nat rule 5007 outbound-interface eth3.181
set service nat rule 5007 protocol all
set service nat rule 5007 type masquerade
set service ssh port 22
set service ssh protocol-version v2
set service unms connection 'wss://10.0.154.3:9443+9exGQ9uBNb03M4Iqwh7AW9852kdaXRVZMFO1eGH_i7wAAAAA+allowSelfSignedCertificate'
set service unms disable
set system conntrack expect-table-size 4096
set system conntrack hash-size 4096
set system conntrack table-size 32768
set system conntrack tcp half-open-connections 512
set system conntrack tcp loose enable
set system conntrack tcp max-retrans 3
set system host-name Bamburi-Gateway
set system login user admin authentication encrypted-password '$5$q8ZKJwmhOJ6ZGuNV$hsJXqIGh03Z0zsO8/xdwLGSwtqSh3ycxLmlYsFQ2WxA'
set system login user admin level admin
set system name-server 8.8.8.8
set system ntp server 0.ubnt.pool.ntp.org
set system ntp server 1.ubnt.pool.ntp.org
set system ntp server 2.ubnt.pool.ntp.org
set system ntp server 3.ubnt.pool.ntp.org
set system syslog global facility all level notice
set system syslog global facility protocols level debug