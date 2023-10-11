from django.urls import path

from stock_monitoring.views import CreateStockMonitor, GetMonitoredStocksList, GetMonitoredStocksChangesHistory, GetMonitoredStocksDetails

urlpatterns = [
    path('create', CreateStockMonitor.as_view(), name='create'),
    path('list', GetMonitoredStocksList.as_view(), name='list'),
    path('history', GetMonitoredStocksChangesHistory.as_view(), name='history'),
    path('details', GetMonitoredStocksDetails.as_view(), name='history'),
]