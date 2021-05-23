from django.test import TestCase

# Create your tests here.

from ..models import Customer, Document
from faker import Faker
import re
from django.conf import settings
from pathlib import Path
import openpyxl
from django.utils import timezone
from django.core.files import File


# locale_list = ['en-US', 'de_DE','en_CA','en_GB','en_AU','fr_FR','it_IT']
# fake = Faker(locale_list)


def parse_fake_address(address):
    # currently only deals with US address - need international faker
    return re.match(
        "(?P<stree1>[\w ]+)\s*(?P<city>\w+),\s*(?P<state>[A-Z]+)\s*(?P<zip>\d+)",
        address,
    )


def translate_company_suffix(cmp_suffix):
    x = fake.company_suffix()


class CustomerModelTests(TestCase):
    pass

    # def test_comp_names(self):
    #     test_companies = [fake.address() for _ in range(10)]

    # def test_phone_nums(self):
    #     test_phone = [fake.phone_number() for _ in range(10)]

    # def test_address_property(self):
    #     test_addresses = [fake.address() for _ in range(10)]


class DocumentModelTests(TestCase):


    def build_test_doc(self, mapping="('A1',customer.comp_name);('A2',customer.post_code);('A3',jap_date)"):
        workbook = openpyxl.Workbook()
        test_filename = "test_file.xlsx"
        workbook.save(filename=test_filename)
        test_doc = Document(
            mapping=mapping,
        )
        with open(test_filename, "rb") as excel:
            test_doc.template.save(test_filename, File(excel))

        test_doc.save()

        return test_doc

    def build_test_cus(self):
        test_customer = Customer(
            comp_name="Test_comp_name",
            email_address="test@gmail.com",
            street1="Test_street1",
            city="Test_city",
            state="Test_state",
            post_code="Test_post_code",
            country="Test_country",
            phone_number="+448765467542",
        )

        test_customer.save()
        return test_customer

    def test_file_location(self):
        """make sure file uploaded to media/temp/filename"""
        test_doc = self.build_test_doc()
        temps_dir = settings.MEDIA_ROOT / "temps"
        assert "test_file.xlsx" in temps_dir.glob("*")

    def test_gen_doc_file_location(self):

        test_doc = self.build_test_doc()
        test_customer = self.build_test_cus()
        test_doc.generate_document(test_customer)
        expected_filename = f"{test_doc.name}-{test_customer.comp_name}-.xlsx"
        gen_dir = settings.MEDIA_ROOT / "generated"
        assert expected_filename in gen_dir.glob("*")

    def test_gen_doc_file_mapping(self):
        # setup
        mapping = "('A1',customer.comp_name);('A2',customer.post_code);('A3',jap_date)"
        test_doc = self.build_test_doc(mapping=mapping)
        test_customer = self.build_test_cus()
        test_doc.generate_document(test_customer)
        expected_filename = f"{test_doc.name}-{test_customer.comp_name}-.xlsx"
        expected_path = settings.MEDIA_ROOT / "generated"

        # test
        workbook = openpyxl.load_workbook(filename=expected_path / expected_filename)
        workbook = workbook.active  # first sheet
        assert workbook["A1"] == test_customer.comp_name
        assert workbook["A2"] == test_customer.post_code
        now = timezone.now()
        jap_date = f"令和{now.year-2018}年{now.month}月{now.day}日"
        assert workbook["A3"] == jap_date
