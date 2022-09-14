from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.pagination import LimitOffsetPagination
from drf.serializers import ProductSearchSerializer
from search.documents import ProductDocument
from elasticsearch_dsl import Q

from rest_framework.response import Response

class SearchProduct(APIView, LimitOffsetPagination):
    product_serializer = ProductSearchSerializer
    product_document = ProductDocument

    def get(self, request, query=None):
        try:

            q = Q('multi_match', query=query, fields=['title','brand',], fuzziness='auto',)
            #)& Q(should=
            #    [Q("match",is_active=True),], 
            #    minimum_should_match=1,
            #    )
            s = self.product_document.search()
            s.query_string = q
            response = s.execute()
            res = self.paginate_queryset(response, request, view=self)
            serializer = self.product_serializer(res, many=True)
            #return Response(serializer.data)
            return self.get_paginated_response(serializer.data)
        except Exception as e:
            return HttpResponse(e, status=500)