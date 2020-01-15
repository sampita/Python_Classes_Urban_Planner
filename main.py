from building import Building

# Creating Your Buildings
# Create 5 building instances
building_1 = Building("3000 Italia Ave, Italy", 80)
building_2 = Building("123 Forrest Ave, Amsterdam", 10)
building_3 = Building("9128 Mercury Road, Tennessee", 80)
building_4 = Building("2008 West Lake Drive, Michigan", 15)
building_5 = Building("1919 Rose Bend Ct, Sussex", 80)

buildings_list = list([building_1, building_2, building_3, building_3, building_4, building_5])
# print(buildings_list)


# Have each one get purchased by a real estate magnate
for building in buildings_list:
    building.purchase("MegaRealEstate Corp LLC")

# After purchased, construct each one
for building in buildings_list:
    building.construct()

# Once all building are purchased and constructed, print the address, owner, stories, and date constructed to the terminal for each one.
for building in buildings_list:
    building.print_statement(building.address, building.owner, building.date_constructed, building.stories)