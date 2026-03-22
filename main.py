import json
import os

DATA_FILE = "crops.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(crops):
    with open(DATA_FILE, "w") as f:
        json.dump(crops, f, indent=4)

def add_crop():
    crops = load_data()
    name = input("Enter crop name: ")
    crop_type = input("Enter crop type (Vegetable/Fruit/Grain): ")
    season = input("Enter season: ")
    soil = input("Enter suitable soil: ")

    crop = {
        "name": name,
        "type": crop_type,
        "season": season,
        "soil": soil
    }
    crops.append(crop)
    save_data(crops)
    print(f"{name} added successfully!")

def view_crops():
    crops = load_data()
    if not crops:
        print("No crops available.")
        return
    print("\n--- All Crops ---")
    for idx, crop in enumerate(crops, start=1):
        print(f"{idx}. {crop['name']} | Type: {crop['type']} | Season: {crop['season']} | Soil: {crop['soil']}")
    print("-----------------\n")

def search_crop():
    crops = load_data()
    name = input("Enter crop name to search: ").lower()
    found = [c for c in crops if c['name'].lower() == name]
    if not found:
        print("Crop not found.")
    else:
        for crop in found:
            print(f"Found: {crop['name']} | Type: {crop['type']} | Season: {crop['season']} | Soil: {crop['soil']}")

def delete_crop():
    crops = load_data()
    view_crops()
    idx = int(input("Enter crop number to delete: ")) - 1
    if 0 <= idx < len(crops):
        removed = crops.pop(idx)
        save_data(crops)
        print(f"{removed['name']} deleted successfully!")
    else:
        print("Invalid selection.")

def menu():
    while True:
        print("\n--- Agriculture CEFP Menu ---")
        print("1. Add Crop")
        print("2. View Crops")
        print("3. Search Crop")
        print("4. Delete Crop")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_crop()
        elif choice == "2":
            view_crops()
        elif choice == "3":
            search_crop()
        elif choice == "4":
            delete_crop()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    menu()