
"""
Inventory Forecasting and Warehouse Simulation
"""
from dataclasses import dataclass
from typing import List
import random

@dataclass
class Product:
    sku: str
    stock: int
    reorder_level: int
    lead_time_days: int

class Warehouse:
    def __init__(self):
        self.products: List[Product] = []

    def add_product(self, product):
        self.products.append(product)

    def simulate_day(self):
        for product in self.products:
            demand = random.randint(1, 15)
            product.stock = max(0, product.stock - demand)

    def reorder_report(self):
        report = []
        for p in self.products:
            if p.stock <= p.reorder_level:
                report.append({
                    "sku": p.sku,
                    "stock": p.stock,
                    "lead_time": p.lead_time_days
                })
        return report

def build_demo():
    wh = Warehouse()
    for i in range(200):
        wh.add_product(
            Product(
                sku=f"SKU-{i:04d}",
                stock=random.randint(50,300),
                reorder_level=40,
                lead_time_days=random.randint(3,14)
            )
        )
    return wh

if __name__ == "__main__":
    warehouse = build_demo()
    for _ in range(30):
        warehouse.simulate_day()

    print("Reorder Items")
    for item in warehouse.reorder_report():
        print(item)
