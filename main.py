import os

def main():
    nombre= os.getenv("USERNAME")
    print(f"Hola mundos {nombre}")

if __name__ == "__main__":
    main()