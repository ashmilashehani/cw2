import Q22
Q22.generate_key()
key = Q22.load_key()

# encrypt file
f = open("Video.mp4", "rb")
Q22.encrypt_message(f.read())
# print(f.read())
f.close()

#decrypt File
f = open('encoded.file','rb')
Q22.decrypt_message(f.read())
f.close()
