for kategori in self.kategorier:    # Looper gjennom nøklene, dvs. 0, 1, 2...
            print(f"Kategori:  {self.kategorier[kategori]}")
            sortert[kategori] = []  # Legger sorterte varer inn i en liste.
            for vare in self.varer:
                if vare.kategori == kategori:
                    sortert[kategori].append(vare)