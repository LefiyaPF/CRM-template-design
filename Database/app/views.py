from django.shortcuts import redirect, render
from app . models import ProductDetails

# Create your views here.

def Home(request):
    return render(request,"Home.html")


def AddProductDetails(request):

    if request.method=='POST':
        pname = request.POST['ProductName']
        Pdescription = request.POST['ProductDescription']
        Pquantity = request.POST['ProductQuantity']
        Pprice= request.POST['ProductPrice']

        Product =  ProductDetails(ProductName = pname,Description = Pdescription,Quatity = Pquantity,Price =Pprice )

        Product.save()

        print("data inserted")

        return redirect('ShowProducts')
    

def ShowProducts(request):

    Products = ProductDetails.objects.all()

    return render(request,"Products.html",{'products':Products})


def EditPage(request,pk):

    Products = ProductDetails.objects.get(id=pk)

    return render(request,"Edit.html",{'products':Products})

def EditProductDetails(request,pk):

    if request.method=="POST":
        Products = ProductDetails.objects.get(id=pk)

        Products.ProductName = request.POST.get('Pname')
        Products.Description = request.POST.get('Pdescription')
        Products.Quatity = request.POST.get('Pquantity')
        Products.Price = request.POST.get('Pprice')

        Products.save()

        return redirect('ShowProducts')
    else:
        return render(request,"Edit.html")

def DeleteItem(request,pk):

    Products = ProductDetails.objects.get(id=pk)

    Products.delete()

    return redirect('ShowProducts')

