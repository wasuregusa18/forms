from forms.views.document_views import CreateDocument
from django.http.request import QueryDict



def test_extract_mapping(self):
    test_doc = CreateDocument()

    # valid
    q = QueryDict("cell1=A4&val1=address&cell2=C33&val2=date&template=morning")
    assert test_doc.extract_mapping(q) == "('A4',customer.address);('C33',customer.date)", "incorrectly parsing"
    
    # numbers don't match
    q1 = QueryDict("cell1=A4&val2=address&cell3=C33&val3=date&template=morning")
    assertRaises(AssertionError, "numbers don't match")

    # not valid cell
    q2 = QueryDict("cell2=4A&val2=address&cell3=C33&val=date&template=morning")
    assertRaises(AssertionError, "not valid cell")

    #missing val
    q3 = QueryDict("cell2=C3&val2=address&cell3=C33")
    assertRaises(AssertionError, "missing corresponding val")

    # not in customer properties
    q4 = QueryDict("cell2=A4&val2=not_address")
    assertRaises(AssertionError, "not in customer properties")

    #order wrong
    q5 = QueryDict("val2=address&cell2=A4")
    assertRaises(AssertionError, "cell val order reserved")
