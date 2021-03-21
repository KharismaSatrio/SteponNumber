#Soal_2
def steponNumber(z): #start function
    x  = z[0]  #disini x mengambil element list terdepan
    y  = z[1]  #disini y mengambil element list terakhir
    if y >= 0 or x >= 0:               #Disini pattern soal terlihat y dan x tidak mungkin negatif
        if x % 2 == 0 and y % 2 == 0 and x>=y:  #Baris 6 memperlihatkan pattern soal dimana X akan ditambah dengan Y jika Y dan X sama-sama bilangan genap dan x lebih besar sama dengan y                  
            a=x+y
            return a
        elif y == 0 and x % 2 == 0 and x>=y:     #Baris 9 memperlihatkan pattern soal dimana X akan ditambah dengan Y jika Y sama dengan 0 dan x adalah bilangan genap dan x lebih besar sama dengan y                        
            a=x+y
            return a
        elif x == 0 and y == 0 and x>=y:         #Baris 12 memperlihatkan pattern soal dimana X akan ditambah dengan Y jika Y dan X bernilai 0 dan x lebih besar sama dengan y
            a=x+y
            return a
        elif x % 2 == 1 and y % 2 == 1 and x>=y: #Disini pattern soal terlihat bahwa jika y dan x merupakan bilangan kelipatan 1,3,5,.. etc dimana semua bilangan itu mempunyai kesamaan yaitu jika dibagi 2 akan selalu menghasilkan 1 dan x lebih besar sama dengan y
            a= x+y-1                    #maka x akan ditambah dengan y dan dikurangi oleh 1
            return a
        elif x == 1 and y == 1 and x>=y: #Disini pattern soal memperlihatkan jika x dan y sama-sama 1 dan x lebih besar sama dengan y
            a= x+y-1             #maka x akan ditambah dengan y dan dikurangi oleh 1
            return a
        elif x % 2 == 1 and y == 1 and x>=y: #Disini pattern soal memperlihatkan jika x adalah nilai yang akan selalu tersisa 1 jika di bagi 2 dan y adalah 1 dan x lebih besar sama dengan y
            a= x+y-1                #maka x akan ditambah dengan y dan dikurangi oleh 1
            return a
        else:
            return ('No Number') #Jika terdapat input yang tidak sesuai dengan pattern pada soal maka akan keluarkan 'No Number'
    else:
        return ('No Number') #Jika terdapat input yang tidak sesuai dengan pattern pada soal maka akan keluarkan 'No Number'

z = [[4,2],[6,6],[3,4]] #Inputan sesuai dengan soal

print(steponNumber(z[0])) #Format penggunaan function mengikuti dengan soal ' print(steponNumber(List_awal)) '
print(steponNumber(z[1]))
print(steponNumber(z[2]))

