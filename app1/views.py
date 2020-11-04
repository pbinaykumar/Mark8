from .serializers import ProductSerializer,VehicleSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product,Vehicle

class index(APIView):
    def post(self,request):
       if request.method == 'POST':
            pi = int(request.data['product_id'])
            if pi == 1:
                price=5
            elif pi == 2:
                price=10

            result = Product.objects.filter(Product_Id=pi)
            serialize = ProductSerializer(result, many=True)
            a = serialize.data
            for i in a:
                moq = i['Minimum_Order_Quantity']
            result = Vehicle.objects.filter(Product_Id=pi, Vehicle_Name='Trolley Truck')
            serialize = VehicleSerializer(result, many=True)
            a = serialize.data
            for i in a:
                ttc = i['Capacity']
            result = Vehicle.objects.filter(Product_Id=pi, Vehicle_Name='Tata Hyva')
            serialize = VehicleSerializer(result, many=True)
            a = serialize.data
            for i in a:
                thc = i['Capacity']

            order_quantity = int(request.data['order_quantity'])
            oq = order_quantity

            if order_quantity >= moq:
                    bill = oq * price
                    abill = int(bill * 0.15)
                    r=order_quantity % thc
                    if r % ttc == 0:
                        return Response({'valid': 'True', 'bill_amount': bill, 'advance_amount': abill})
                    elif order_quantity % ttc == 0:
                        return Response({'valid': 'True', 'bill_amount': bill, 'advance_amount': abill})
                    else:
                       return Response({'valid': 'False'})
            else:
                return Response({"'valid':'False'"})
       else:
           return Response('Only POST Methode Is Acceptable')