from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import TestModelSerializer,TestModelGetSerializer
from .models import TestModel

# get all data
class GetAllData(APIView):
    def get(self,request):
        data = TestModel.objects.all()
        serializeData= TestModelGetSerializer(data,many=True)
        return Response(serializeData.data)

# add new data
class AddNewData(APIView):
    def post(self,request):
        newData = TestModelSerializer(data=request.data)
        if newData.is_valid():
            newData.save()
            return Response(newData.data)
        else:
            return Response({"msg":"invalid data"})

# update data
class UpdateData(APIView):
    def patch(self,request,id):
        dataToUpdate = TestModel.objects.get(id=id)
        if dataToUpdate:
            newData = TestModelSerializer(dataToUpdate,data=request.data)
            if newData.is_valid():
                newData.save()
                return Response({"msg":"updated successfully.","data":newData.data})
            else:
                return Response({"msg":"invalid data"})    
        else:
            return Response({"msg":"invalid id"})  


# delete data
class DeleteData(APIView):
    def delete(self,request,id):
        dataToDelete = TestModel.objects.get(id=id)
        if dataToDelete:
            dataToDelete.delete()
            return Response({"msg":"deleted successfully.","id":id})
        else:
            return Response({"msg":"invalid id"})    
