"""
Models
"""
from django.db import models

class BaseModel(models.Model):
    """
    Abstract base model to handle status and keep track of the last change
    """
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_enable = models.BooleanField(default=True)
    created_by = models.ForeignKey('base.User',
                                    on_delete=models.PROTECT,
                                    related_name='%(app_label)s_%(class)s_creates')
    updated_by = models.ForeignKey('base.User',
                                    on_delete=models.PROTECT,
                                    related_name='%(app_label)s_%(class)s_actualiza')


    class Meta:
        """Abstract class"""
        abstract = True


class TransportCompany(BaseModel):
    """Transport company"""
    name = models.CharField(max_length=50)


class Vehicle(BaseModel):
    """Vehicle"""
    plate = models.CharField(max_length=50, null=True, blank=True)
    company = models.ForeignKey('TransportCompany',
                                on_delete=models.PROTECT,
                                null=True,
                                blank=True,
                                related_name='+')

class Driver(BaseModel):
    """Driver"""
    vehicle = models.ForeignKey('Vehicle',
                                 on_delete=models.PROTECT,
                                 null=True,
                                 blank=True,
                                 related_name='+')
    company = models.ForeignKey('TransportCompany',
                                on_delete=models.PROTECT,
                                null=True,
                                blank=True,
                                related_name='+')

class Producer(BaseModel):
    """Producer"""
    code = models.CharField(max_length=20)

class Plantation(BaseModel):
    """Plantation"""
    producer = models.ForeignKey('Producer',
                                 on_delete=models.PROTECT,
                                 null=True,
                                 blank=True,
                                 related_name='plantations')

class Brand(BaseModel):
    """Brand"""
    name = models.CharField(max_length=50)
    producer = models.ForeignKey('Producer',
                                 on_delete=models.PROTECT,
                                 null=True,
                                 blank=True,
                                 related_name='brands')

class BoxType(BaseModel):
    """Box type"""
    name = models.CharField(max_length=50)


class Port(BaseModel):
    """Port"""
    name = models.CharField(max_length=50)


class Process(BaseModel):
    """Process"""
    producer = models.ForeignKey('Producer',
                                 on_delete=models.PROTECT,
                                 null=True,
                                 blank=True,
                                 related_name='processes')
    vehicle = models.ForeignKey('Vehicle',
                                on_delete=models.PROTECT,
                                null=True,
                                blank=True,
                                related_name='processes')
    driver = models.ForeignKey('Driver',
                               on_delete=models.PROTECT,
                               null=True,
                               blank=True,
                               related_name='processes')
    transport_company = models.ForeignKey('TransportCompany',
                                          on_delete=models.PROTECT,
                                          null=True,
                                          blank=True,
                                          related_name='processes')


class Inspection(BaseModel):
    """Inspection"""
    process = models.ForeignKey('Process',
                                on_delete=models.PROTECT,
                                null=True,
                                blank=True,
                                related_name='inspections')
