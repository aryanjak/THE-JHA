aT = "sl.BDErRMDz2hu31NtdhxpI_ZI9yCWzfOArq8_8FqXSkIwlqp79WkyY-rQXRY_hNsC_Rj4Yk-Ons2kS5l9HpB68BfMYdsIRkgl5k9VzlKQ0PWzt6iFWpkHlbOT9QTAB7li-F3306S9b6ttH"
import dropbox

dbx = dropbox.Dropbox(aT)
f = open("E:/PYTHON__/C101/file.txt" , 'rb')

dbx.files_upload(f.read() , "THE Jai Hind APE/file.txt")