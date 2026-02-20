import pyscript as py

def document(file, writes):
    with open(f"{file}.txt","w") as file:
        file.write(writes)