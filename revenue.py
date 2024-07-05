import matplotlib.pyplot as plt

data = {
    'cash': 942.498,
    'todayCash': 9053.299,
    'Rev00016': 348.8300000005,
    'Rev00013': 31.99993,
    'Rev00015': 92.36,
    'Rev00017': 287.34,
    'Rev00020': 296.1,
    'Rev00018': 47.54,
    'Rev00045': 77.00
}

revTypes = {
    "Rev00016": {"name": "Petty cash", "connectedTo": "Physical"},
    "Rev00013": {"name": "Debit card", "connectedTo": "HDFC"},
    "Rev00015": {"name": "PhonePe", "connectedTo": "ICICI"},
    "Rev00017": {"name": "Google pay", "connectedTo": "SBI"},
    "Rev00020": {"name": "UPI", "connectedTo": "ICICI"},
    "Rev00018": {"name": "Credit card", "connectedTo": "SBI"}
}
total_revenue = 0.0
for key, value in data.items():
  total_revenue += value
  if not value:
    break

print(f"Total Revenue: {round(total_revenue, 3)}")

mapped_revenues = {revTypes[key]['name']: value for key, value in data.items() if key in revTypes}

all_data_rounded = {key: round(value, 3) for key, value in data.items()}
labels = list(all_data_rounded.keys())
values = list(all_data_rounded.values())

print(labels, values)

plt.figure(figsize=(10, 5))
plt.bar(labels, values, color='lightgreen')
plt.xlabel('Types')
plt.ylabel('Values')
plt.title('Revenue and Other Values')
plt.xticks(rotation=40, ha="right")
plt.tight_layout()
plt.show()


def get_rev_name(revId):
    return revTypes[revId]["name"] if revId in revTypes else None

print(get_rev_name("Rev00020"))
print(get_rev_name("Rev00015"))
