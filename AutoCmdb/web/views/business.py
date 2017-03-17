#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.views import View
from django.shortcuts import render
from django.http import JsonResponse

from web.service import business


class BusinessListView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'business_list.html')


class BusinessJsonView(View):
    def get(self, request):
        obj = business.Business()
        response = obj.fetch_businesses(request)
        return JsonResponse(response.__dict__)

    def delete(self, request):
        response = business.Business.delete_assets(request)
        return JsonResponse(response.__dict__)

    def put(self, request):
        response = business.Business.put_businesses(request)
        return JsonResponse(response.__dict__)


class AssetDetailView(View):
    def get(self, request, device_type_id, asset_nid):
        response = business.Business.businesses_detail(device_type_id, asset_nid)
        return render(request, 'business_detail.html', {'response': response, 'device_type_id': device_type_id})


class AddAssetView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'add_business.html')