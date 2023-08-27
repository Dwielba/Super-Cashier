class Transaction:
    def __init__(self):
        self.items = []

    def add_item(self, item_data):
        self.items.append(item_data)

    def update_item_name(self, old_name, new_name):
        for item in self.items:
            if item[0] == old_name:
                item[0] = new_name

    def update_item_qty(self, name, new_qty):
        for item in self.items:
            if item[0] == name:
                item[1] = new_qty

    def update_item_price(self, name, new_price):
        for item in self.items:
            if item[0] == name:
                item[2] = new_price

    def delete_item(self, name):
        self.items = [item for item in self.items if item[0] != name]

    def reset_transaction(self):
        self.items = []

    def check_order(self):
        for item in self.items:
            if any(element == "seee" for element in item):
                return "Terdapat kesalahan input data"
        return "Pemesanan sudah benar"

    def print_transaction(self):
        print("| No | Nama Item | Jumlah Item | Harga/Item | Total Harga |")
        for i, item in enumerate(self.items, start=1):
            total_harga = item[1] * item[2]
            print(f"| {i} | {item[0]} | {item[1]} | {item[2]} | {total_harga} |")

    def total_price(self):
        total = sum(item[1] * item[2] for item in self.items)
        if total > 500000:
            return total * 0.9
        elif total > 300000:
            return total * 0.92
        elif total > 200000:
            return total * 0.95
        else:
            return total


# Membuat objek dari class Transaction
trnsct_123 = Transaction()

# Menambahkan item belanja
trnsct_123.add_item(["Mobil", 2, 100000])
trnsct_123.add_item(["Mie", 1, 1500])
trnsct_123.add_item(["Tempe", 3, 3000])

# Menambahkan item baru menggunakan metode add_item()
trnsct_123.add_item(["Ayam Goreng", 2, 20000])
trnsct_123.add_item(["Pasta gigi", 3, 15000])

# Menghapus item belanja menggunakan metode delete_item()
trnsct_123.delete_item("Pasta gigi")

# Melakukan perubahan pada item belanja
trnsct_123.update_item_name("Mie", "Indomie")
trnsct_123.update_item_qty("Mobil", 3)
trnsct_123.update_item_price("Tempe", 3500)

# Menghapus item belanja
trnsct_123.delete_item("Mie")

# Melakukan pengecekan pemesanan
print(trnsct_123.check_order())

# Menampilkan transaksi
trnsct_123.print_transaction()

# Menghitung total harga dengan diskon
total = trnsct_123.total_price()
print(f"Total belanja dengan diskon: {total}")