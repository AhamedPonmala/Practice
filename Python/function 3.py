def flash_file(file_name, partitions):
    print(f"\nFlashing {file_name}...")
    for block in range(1, partitions+1):
        print(f"Writing block {block}...")
    print("Success!\n")
flash_file("Boot.img", 3)
flash_file("System.img", 5)