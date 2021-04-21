import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token
    def uploadFile(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)
        with open(file_from,'rb') as f:
            dbx.files_upload(f.read(),file_to)

def main():
    #access_token='sl.At7CR4b-6PAodf2x_W__Tv-jec3qtFt_pAr_IaZQXihx5BXR1b4YeoEH4LKECSdaPLag-KtQqAdfxgYyiRMjznqwYDILAsFd-SBGV3mI9Yi-e8z2gfQyrgSxMAPONZgQiB_EDvQ'
    access_token='sl.At6jvwx7_fuVQ9aRYfnX_oYW_dYXiCANnWk7kj0KC4GNdU9CZJBLi_aVHSH8qu8W3y4ZUEWDLA4RIlEBxXQaopwtGY0rr5Cy-91C_Pb6CTl0VaSDaWpxdI72zkUolIJ29akjXhU'
    transfer_data=TransferData(access_token)
    file_from=input('Enter the file to be transferred ')
    file_to=input('Enter the full path to upload to the dropbox ')
    #file_from='/Users/Siddhant/Documents/pictures/d.jpg'
    #file_to='/Grade 10/d.jpg'
    transfer_data.uploadFile(file_from,file_to)
    print("File has been successfully moved")

main()