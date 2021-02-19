from .models import EtranLoan, Demographics, Race, LookupDisbursedPPPLoan, ForgivenessDocs
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import EtranLoanSerializer, LookupDisbursedPPPLoanSerializer, ForgivenessDocsSerializer


class EtranLoanViewSet(viewsets.ModelViewSet):
    queryset = EtranLoan.objects.all()
    serializer_class = EtranLoanSerializer
    permission_classes = [permissions.IsAuthenticated]


class LookupDisPPPLoanViewSet(viewsets.ModelViewSet):
    queryset = LookupDisbursedPPPLoan.objects.all()
    serializer_class = LookupDisbursedPPPLoanSerializer
    permission_classes = [permissions.IsAuthenticated]


class ForgivenessDocsViewSet(viewsets.ModelViewSet):
    queryset = ForgivenessDocs.objects.all()
    serializer_class = ForgivenessDocsSerializer
    permission_classes = [permissions.IsAuthenticated]
