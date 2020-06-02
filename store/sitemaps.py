from django.contrib.sitemaps import Sitemap

from businessdirectory.models import EquipmentType, Equipment, FillingStation, FillingStationDirectory, \
    FinancialInstitutionDirectory, FinancialInstitution, Transportation, Training, MotorisedService, AutoEngineering, \
    EarthMoving
from store.models import Product, Category, Event, EventType


class ProductsSitemap(Sitemap):

    def items(self):
        return Product.objects.all()


class ProductCategorySitemap(Sitemap):

    def items(self):
        return Category.objects.all()


class EquipmentsSitemap(Sitemap):

    def items(self):
        return Equipment.objects.all()


class EquipmentCategorySitemap(Sitemap):

    def items(self):
        return EquipmentType.objects.all()


class FillingStationsSitemap(Sitemap):

    def items(self):
        return FillingStation.objects.all()


class FillingStationDirectorySitemap(Sitemap):

    def items(self):
        return FillingStationDirectory.objects.all()


class FinancialInstitutionsSitemap(Sitemap):

    def items(self):
        return FinancialInstitution.objects.all()


class FinancialInstitutionDirectorySitemap(Sitemap):

    def items(self):
        return FinancialInstitutionDirectory.objects.all()


class EventsSitemap(Sitemap):

    def items(self):
        return Event.objects.all()


class EventtypesSitemap(Sitemap):

    def items(self):
        return EventType.objects.all()


class MotorizedServicesSitemap(Sitemap):

    def items(self):
        return MotorisedService.objects.all()


class AutoEngineeringServicesSitemap(Sitemap):

    def items(self):
        return AutoEngineering.objects.all()


class EarthMovingServicesSitemap(Sitemap):

    def items(self):
        return EarthMoving.objects.all()


class TrainingServicesSitemap(Sitemap):

    def items(self):
        return Training.objects.all()


class TransportationServicesSitemap(Sitemap):

    def items(self):
        return Transportation.objects.all()