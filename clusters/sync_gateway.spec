[clusters]
sync_gateway =
    172.23.96.64:8091
    172.23.96.65:8091
    172.23.96.62:8091

[storage]
data = /data
index = /data

[credentials]
rest = Administrator:password
ssh = root:couchbase

[gateways]
hosts =
    172.23.96.66
    172.23.96.67

[gateloads]
hosts =
    172.23.96.63
    172.23.96.68

[parameters]
Platform = Physical
OS = CentOS 6.5
CPU = Intel Xeon E5-2630 v2 (24 vCPU)
Memory = 64 GB
Disk = HDD
