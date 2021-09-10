import os
path=r'C:\Users\atefe\Downloads\curriculum_vitae_data-master\curriculum_vitae_data-master\pdf'
def pdf_path(path,n):
    myFiles=[]
    file_path=[]
    for i in range(1,n+1):
        pdf=f'{i}.pdf'
        myFiles.append(pdf)

    for filename in myFiles:
        file=os.path.join(path, filename)
        file_path.append(file)
    return(file_path)

print(pdf_path(path,2))