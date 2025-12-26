data = """Hammer,ZoneA,100,50
Drill,ZoneB,20,10
Saw,ZoneA,30,15
Nails,ZoneC,200,300
Screws,ZoneB,10,10
Corrupt,Line,Error
Paint,ZoneC,40,5"""
with open("warehouse_stock.txt", "w") as file1:
    file1.write(data)

def audit_inventory(filename):
    zone_totals ={}
    low_stock_items = []
    with open(filename, "r") as file2:
        for line in file2:
            parts = line.strip().split(",")
            if len(parts) != 4:
                continue
            product, zone, shelfqty, backroomqty = parts
            try:
                shelfqty = int(shelfqty)
                backroomqty = int(backroomqty)
            except ValueError:
                continue
            total_stock = shelfqty + backroomqty
            if zone not in zone_totals:
                zone_totals[zone] = total_stock
            else:
                zone_totals[zone] += total_stock
            if total_stock < 50:
                low_stock_items.append((product, total_stock))
    return zone_totals, low_stock_items

def generate_reorder_list(zone_totals, low_stock_items):
    with open('inventory_report.txt', "w") as file3:
        file3.write("ZONE INVENTORY COUNTS\n")
        file3.write("---------------------\n")
        for zone, total in zone_totals.items():
            file3.write(f"{zone}: {total}\n")
        file3.write("\nREORDER ALERTS (< 50 items)\n")
        file3.write("---------------------\n")
        for product, total in low_stock_items:
            file3.write(f"{product} ({total} items)\n")

zone_totals, low_stock_items = audit_inventory("warehouse_stock.txt")
generate_reorder_list(zone_totals, low_stock_items)