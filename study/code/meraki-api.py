import meraki

# Instantiate Meraki API Session
dashboard = meraki.DashboardAPI()

orgs = dashboard.organizations.getOrganizations()

for org in orgs:
    print(org['name'])
