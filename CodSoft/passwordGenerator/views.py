from django.shortcuts import render

def passgen(request):
    genpassword=''
    uname =''
    length = 0
    if request.POST:
        uname = request.POST['uname']
        length = int(request.POST['length'])
        import string
        import random
        all_chars = string.ascii_letters + string.digits + string.punctuation
        all_chars = ''.join(char for char in all_chars if char not in '|l1o0O')
        genpassword = ''.join(random.choice(all_chars) for _ in range(length))

    return render(request,'passgen.html',{'uname':uname,'len':length,'pass':genpassword})