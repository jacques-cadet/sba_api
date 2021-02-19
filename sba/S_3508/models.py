from django.db import models


class EtranLoan(models.Model):
    bank_notional_amount = models.FloatField()
    sba_number = models.CharField(max_length=10)
    loan_number = models.CharField(max_length=7)
    entity_name = models.CharField(max_length=120)
    ein = models.CharField(max_length=11)
    funding_date = models.DateField()
    forgive_payroll = models.FloatField()
    naics_code = models.IntegerField()
    ppp_loan_draw = models.IntegerField()
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    dba_name = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=11)
    forgive_fte_at_loan_application = models.IntegerField()
    forgive_amount = models.FloatField()
    forgive_fte_at_forgiveness_application = models.IntegerField()
    forgive_covered_period_from = models.DateField()
    forgive_covered_period_to = models.DateField()
    forgive_2_million = models.BooleanField(default=False)
    primary_email = models.EmailField()
    primary_name = models.CharField(max_length=50)
    ez_form = models.BooleanField(default=False)
    forgive_lender_confirmation = models.BooleanField()
    forgive_lender_decision = models.IntegerField()
    s_form = models.BooleanField()


class Demographics(models.Model):
    etranLoan = models.ForeignKey(EtranLoan, on_delete=models.CASCADE)
    name = models.CharField(max_length=75, blank=True, null=True)
    position = models.CharField(max_length=75, blank=True, null=True)
    veteran_status = models.CharField(max_length=1, blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, null=True)
    ethnicity = models.CharField(max_length=1, blank=True, null=True)


class Race(models.Model):
    dem = models.ForeignKey(Demographics, on_delete=models.CASCADE)
    race = models.CharField(max_length=1, blank=True, null=True)


class ForgivenessDocs(models.Model):
    etranLoan = models.ForeignKey(EtranLoan, on_delete=models.CASCADE)
    document = models.FileField(max_length=100, blank=True, null=True)


class LookupDisbursedPPPLoan(models.Model):

    organization_name = models.CharField(max_length=100)
    bank_notional_amount = models.FloatField()
    sba_number = models.CharField(max_length=50)
    entity_name = models.CharField(max_length=75)
    ein = models.CharField(max_length=11)
    funding_date = models.DateField()
    tin_type = models.IntegerField()
    ppp_loan_draw = models.IntegerField()
    forgive_eidl_amount = models.FloatField()
    eidl_details = models.CharField(max_length=100)

