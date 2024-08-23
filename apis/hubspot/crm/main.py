import os

from hubspot import HubSpot
from hubspot.crm.contacts import SimplePublicObjectInputForCreate
from hubspot.crm.contacts.exceptions import ApiException

token = os.getenv("HUBSPOT_API_KEY")

client = HubSpot(access_token=token)

try:
    props = SimplePublicObjectInputForCreate(
        properties={
            "email": "test@test.com",
        }
    )
    resp = client.crm.contacts.basic_api.create(simple_public_object_input_for_create=props)
except ApiException as e:
    print("Exception when calling ContactsApi->create_contact: %s\n" % e)
