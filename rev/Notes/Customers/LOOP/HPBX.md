# Overview
LOOP is looking to replace their Avaya PBX with a hosted solution.  As is typical for LOOP, there are strict requirements in place for network redundancy/resiliency.  In particular, they have 4 key sites that they have these requirements for:
1) [[Customers/LOOP/Locations/Operations Center|Operations Center]]
2) [[Customers/LOOP/Locations/LOCAP|LOCAP]]
3) [[Customers/LOOP/Locations/HQ|HQ]]
4) [[Customers/LOOP/Locations/Marine Terminal|Marine Terminal]]

LOOP require SIP Survivability and redundant uplinks for each of the above sites. 

# SIP Survivability
SIP Survivability is defined as the ability to make phone calls locally within a facility/network even though connectivity to the remote, cloud-based PBX is down.  This requires a device on-prem that phones can register to should the upstream service be down.

To provide SIP survivability, we are deploying the [[Edgemarc 2900 SBCs|Edgemarc 2900E]] for the first time.  In lab testing, these devices have been capable of handling 100+ SIP registrations and phone calls and passed tests.  

The Edgemarc 2900E can provide SIP Survivability in "Transparent" mode, which uses the SIP ALG to monitor VOIP traffic and have the phones register locally when there is no link to the Perimeta.  This enables SIP Survivability without having to register the phones locally on the Edgemarc, which is a big advantage for deployment & support over the older [[Devices/Adtran/Total Access|TA908e]] that we've used previously.

# Locations
## Operations Center/OC/Galliano
### Info
- This location has an ASR920, a link to LOOP's microwave network, and a link to their satellite network. 

## LOCAP / St. James
### Address
### Info
- This location has an ASR920, a link to LOOP's microwave network?, and a link to their satellite network?

## Covington/HQ
### Address
### Info
- This location has an ASR920, and a link to their satellite network?

## Marine Terminal
### Address
### Info
- This location is about 15 miles offshore from the Fourchon station.  This will require LOOP to build us two VLANs for diverse microwave network routes to the terminal, and a link to their satellite network.

# Redundancy
In addition to the terrestrial WAN network that we provide, LOOP also has a microwave network and satellite backup.  LOOP would like for us to integrate into all 3 networks to have failover capabilities should there be outages.  LOOP has been through a lot of with storms and we all learned how valuable that level of redundancy is when something like Hurricane Ida rolled through in 2021.

The Edgemarc devices do have robust routing capabilities, however they only have 2 WAN links and do not meet our needs.  Because LOOP has 3 networks, we need a device that can handle at least 3 uplinks.  To facilitate three uplinks, with the third being an internet connection, we will use the [[Devices/Juniper/SRX320|Juniper SRX320]] to route.  

### Routing Information
The SRX320 will run [OSPF](https://en.wikipedia.org/wiki/Open_Shortest_Path_First) with the local ASR920 at each site and another ASR920 at another site through the LOOP-provided microwave network link, and we will have to advertise the local gateway IP of the SRX to our core.  We will disable NAT on traffic heading out towards these two links as they will be on our backbone.

In addition, there will be a 3rd link that uses the LOOP satellite internet as a failsafe.  We will need to set up another security zone for this route so that when traffic fails over to it, it NATs through that public IP.

# Monitoring/Visibility
We will deploy a [[Devices/Ubiquiti/UDM|UDM]] that runs [DHCP](https://en.wikipedia.org/wiki/Dynamic_Host_Configuration_Protocol) for the phones.  This enables the [UDM portal](https://account.ui.com/login?redirect=https%3A%2F%2Funifi.ui.com%2Fdashboard) to be the front end to gain visibility into the network to do basic troubleshooting at lower tier support levels, rather than every phone problem being punted to IP Operations. 

This, however, is not without its drawbacks.  This requires us to have the UDM to do DHCP and the Edgemarc to be the gateway of the network, separating those roles.

## Early Diagram
![[Pasted image 20240206195418.png]]



# To-Dos
- [x] Talk to LOOP about the satellite links to ensure they are public internet-based 📅 2024-02-08 ✅ 2024-02-16
- [x] Talk to Eddie or LOOP about where microwave links are available 📅 2024-02-08 ✅ 2024-02-16
- [x] Talk to Eddie or LOOP about OC and where we'll need to use LOOP fiber 📅 2024-02-08 ✅ 2024-02-16
- [x] Talk to Eddie about whether we'd be bringing in our own switches or using LOOP switches. 📅 2024-02-08 ✅ 2024-02-16