import dropbox


class TransferData:
    def __init__(self,access_token):
        self.access_token =access_token


    def upload_file(self,file_from,file_to):
        
            dbx = dropbox.Dropbox(self.access_token)       
            f = open(file_from,"rb")
            dbx.files_upload(f.read(), file_to)

def main():
        access_token = 'sl.AsS7qr2vYa5y_SoWIJdEeamdVWUsEb2MLNdo3JCW8vovewsDCSX7gFlF-47eWYPR5xrfDCFotqixwRdXEanmYAZJOe15qqqWwsPovbPoo0qReB4c16PaK6h9wAFdXSDeW3PC2lI'
        transferData = TransferData(access_token)

        file_from=input("enter the file path to trasfer ")
        file_to=input("enter the full path to upload to dropbox ")
        transferData.upload_file(file_from, file_to)
        print("file has been moved")
    
main()