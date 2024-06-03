import os

def main():
    nombre= os.getenv("USERNAME")
    print(f"Hola mundo {nombre}")

if __name__ == "__main__":
    main()