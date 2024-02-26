# Pre-Sale Engineering
Potential WAN, DIA, & POTS customer.

Customer desires as much diversity of COs among sites as possible.  For example, the 1233 & 1309 Canal Blvd locations should work out of TBDO and HOMA, respectively.  The rest of the sites we may have to split up among TBDO and HOMA, and maybe LKPT if we can get circuits there.

In addition, each site needs POTS, so we'll need a minimum of 2 fibers per location.  One for Metro-E Services, one for POTS lines.  

WAN consists of the following locations:

|**Location**|**Service Address**|**Network Service**|**REV Service**|**MRC**|
|:---:|:---:|:---:|:---:|:---:|
|Thibodaux Water Plant|110 E Bayou Rd  <br>Thibodaux, LA 70301|1 Gig Port Connection & 4 MB|20 Mbps WAN|$315.00|
|VCH Building|112 St. Mary St.  <br>Thibodaux, LA|1 Gig Port Connection & 10 MB|20 Mbps WAN|$315.00|
|Public Works|1219 Henry Schuyler Thibodaux St.  <br>Thibodaux, LA|1 Gig Port Connection & 20 MB|50 Mbps WAN|$390.00|
|General Administration|1233 Canal Blvd.  <br>Thibodaux, LA|1 Gig Port Connection & 50 MB|100 Mbps WAN|$550.00|
|General Administration|1233 Canal Blvd.  <br>Thibodaux, LA|ADI Accesss - 100 MB  <br>& Managed Router|100 Mbps DIA/Managed Router|$725.00|
|Stark Municipal Complex|1309 Canal Blvd  <br>Thibodaux, LA.|1 Gig Port Connection & 10 MB|20 Mbps WAN|$315.00|
|Stark Municipal Complex|1309 Canal Blvd  <br>Thibodaux, LA.|ADI Accesss - 50 MB  <br>& Managed Router|50 Mbps DIA|$550.00|
|Martin Luther King Park|1445 Martin Luther King Dr.  <br>Thibodaux, LA|1 Gig Port Connection & 4 MB|20 Mbps WAN|$315.00|
|Peltier Park Pavilion and Building|151 Peltier Park Dr. OR 151 Cherokee Ave.  <br>Thibodaux LA, 70302|1 Gig Port Connection & 10 MB|20 Mbps WAN|$315.00|
|Thibodaux Sewage Plant (South Plant)|198 J David Bergeron Rd  <br>Thibodaux, LA|1 Gig Port Connection & 10 MB|20 Mbps WAN|$315.00|
|North Sewer Plant|2400 Rosedown Dr.  <br>Thibodaux, LA|1 Gig Port Connection & 1000 MB|1 Gbps WAN|$950.00|
|Warren J. Harang Municiple Auditorium|310 North Canal Blvd.  <br>Thibodaux, LA 70301|1 Gig Port Connection & 10 MB|20 Mbps WAN|$315.00|
|City Hall|310 W. 2nd St.  <br>Thibodaux, LA 70301|1 Gig Port Connection & 50 MB|100 Mbps WAN|$550.00|
|City Hall|310 W. 2nd St.  <br>Thibodaux, LA 70301|ADI Accesss - 20 MB  <br>& Managed Router|20 Mbps DIA/Managed Router|$425.00|
|Thibodaux Municipal Pool,|737 Goode Street  <br>Thibodaux, LA|No Network Connection|||
|Andolsek Park|1200 North Canal Blvd.  <br>Thibodaux, LA||||


## Clarifications Needed
- "Managed Router" - A Firewall?  How do they handle internet routing?  They will have 2 DIAs, one at City Hall, and one at Stark Municipal Complex, so they've got to do some sort of routing/load balancing.  We cannot offer that service.  Eddie's got a note that they need a block of 15 IPs - a /28.  Perhaps this would be a shared gateway scenario?

### Eddie Responded
Yes, managed firewall (actually have a third location as well).  Separate IP space.  The goal is simply to service the 2 locations from unique offices.