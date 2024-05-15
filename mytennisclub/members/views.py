from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Member


def members(request):
  if request.method == "POST":
    firstname = request.POST.get("firstname")
    lastname = request.POST.get("lastname")
    phone = request.POST.get("phone")
    joined_date = request.POST.get("joined_date")
    hobbies = request.POST.get("hobbies")  
    
    Member.objects.create(
      firstname = firstname,
      lastname = lastname,
      phone = phone,
      joined_date = joined_date,
      hobbies = hobbies
    )   

  queryset=Member.objects.all()
  
  search_query = request.GET.get('search')
  if search_query:
      queryset = queryset.filter(
          Q(firstname__icontains=search_query) |
          Q(lastname__icontains=search_query) |
          Q(phone__icontains=search_query) |
          Q(joined_date__icontains=search_query) |
          Q(hobbies__icontains=search_query)
      )
    
  context = {'members' : queryset}
  return render(request, 'all_members.html', context)
  

def add_member(request):
  if request.method == "POST":
    firstname = request.POST.get("firstname")
    lastname = request.POST.get("lastname")
    phone = request.POST.get("phone")
    joined_date = request.POST.get("joined_date")
    hobbies = request.POST.get("hobbies")  
    
    Member.objects.create(
      firstname = firstname,
      lastname = lastname,
      phone = phone,
      joined_date = joined_date,
      hobbies = hobbies
    )    
    return redirect('/members/')
  
  queryset = Member.objects.all()
  context = {'members' : queryset}

  return render(request, 'add_member.html', context)


def update_member(request, id):
  queryset = Member.objects.get(id=id)
  if request.method == "POST":
    firstname = request.POST.get("firstname")
    lastname = request.POST.get("lastname")
    phone = request.POST.get("phone")
    joined_date = request.POST.get("joined_date")
    hobbies = request.POST.get("hobbies")  
    
    queryset.firstname = firstname
    queryset.lastname = lastname
    queryset.phone = phone
    queryset.joined_date = joined_date
    queryset.hobbies = hobbies
    
    queryset.save()
    return redirect('/members/')
  context = {'members' : queryset}
  
  return render(request, 'update_members.html', context)

  
def delete_member(request, id):
    queryset = Member.objects.get(id=id)
    if request.method == 'POST':
        if request.POST.get('confirm') == 'Yes':
            queryset.delete()
            return redirect('/members/')
        else:
            return render(request, 'all_members.html')
    else:
        return render(request, 'confirm_delete.html')

    
  

