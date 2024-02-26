# Overview

## Network Design

TGHS has an ASR920 deployed on site at the main hospital (10.3.254.8) to aggregate handoff of services as well as provide diverse, redundant uplinks for the majority of services. The ASR920 is uplinked to HOMA and TBDO CEs via 2 sets of 2Gb LAGs.

# Main Hospital

### Service addresses

Main campus - 8166 Main St Houma, LA 70360

Atrium Services - 855 Bellanger St. Ste. 108 Houma, LA 70360

## Diagram
![[Pasted image 20240209115923.png]]
## ASR920 Service Information

|   |   |   |   |
|---|---|---|---|
|**ASR920 Port**|**SA**|**CID**|**Service Description**|
|BDI100|1085937|30 METRO 1742..EC|TGHS Internet|
|Gi/0/0/0|1338038|30 METRO 1742..EC_A|TGHS Internet Handoff #1|
|Gi0/0/1|1092972|30 METRO 1742..EC_C|HPBX UDM PRO|
|Gi0/0/2|1338039|30 METRO 1742..EC_B|TGHS Internet Handoff #2|
|Gi0/0/3|1119843|30 METRO 1852..EC_A|Link to WAN|
|Gi0/0/10|1234986|30 METRO 2074..EC|DIA for SIP Trunk|
|Gi0/0/20|1238143|30 MPLS TGMC TBDO1|Member of PO5|
|Gi0/0/21|1238146|30 MPLS TGMC TBDO2|Member of PO5|
|Gi0/0/22|1238139|30 MPLS TGMC HOMA1|Member of PO15|
|Gi0/0/23|1238097|30 MPLS TGMC HOMA2|Member of PO15|
|Te0/0/24|1338249|30 METRO 2533..EC|CPE Palo Alto Handoff #1|
|Te0/0/25|1338250|30 METRO 2534..EC|CPE Palo Alto Handoff #2|
|Te0/0/27|1116972|30 WAVE 0017..EC_A|Wave Uplink|

## PON/Voice Services

|   |   |   |   |
|---|---|---|---|
|**SA#**|**CID**|**SLID**|**Description**|
|1235457|30 DHDV 6319|N/A|PRI fed from Schriever TA5K|
|1261557|30 DHDV 6344|HOMA101320|PRI fed from HOMA GPON|
|1085940|N/A|N/A|Main Campus MLAN|
|1233482|TBDO113115|TBDO113115|Atrium HVN|

# Gray Clinic

## Service Address

115 Eureka Dr. Gray, LA 70359

## Services

|   |   |   |   |
|---|---|---|---|
|**SA#**|**CID**|**SLID**|**Description**|
|1119844|30 METRO 1852..EC_B|N/A - Served via SCHV TA5K|Link to WAN|

# Diagnostic Center

## Service Address

316 Civic Center Blvd, Houma, LA 70360

## Services

|   |   |   |   |
|---|---|---|---|
|**SA#**|**CID**|**SLID**|**Description**|
|1291442|316 CIVIC CENTER BLVD|HOMA102603|Link to WAN|

# Contacts
Derrick bonvillian
985-855-4398 cell
985-873-3486 office