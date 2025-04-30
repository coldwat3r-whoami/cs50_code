def main():

    file = input("File name: ").strip(" ").lower()
    extension = file.split(".")

    if file.endswith("gif") or file.endswith("png"):
        print("image/"+extension[1])
    elif file.endswith("jpg") or file.endswith("jpeg"):
        print("image/jpeg")
    elif file.endswith("txt"):
        print("text/plain")
    elif file.endswith("pdf"):
        print("application/pdf")
    elif file.endswith("zip"):
        print("application/zip")
    elif file.endswith(""):
        print("application/octet-stream")
        return

main()
