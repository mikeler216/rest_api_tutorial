from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Bucketlist
from rest_framework.test import APIClient
from rest_framework import status


# Create your tests here.


class ModelTestCase(TestCase):
    """
    This class will hold the test suite for the bucketlist model.
    """

    def setUp(self) -> None:
        """
        Define the test client and other test variables.
        """
        self.bucketlist_name: str = "Write world class code"
        self.user = User.objects.create(username="nerd")
        self.bucketlist: Bucketlist = Bucketlist(name=self.bucketlist_name, owner=self.user)

    def test_model_can_create_a_bucklist(self):
        """
        Test the bucketlist model can create a bucketlist
        :return:
        """
        old_count: int = Bucketlist.objects.count()
        self.bucketlist.save()
        new_count: int = Bucketlist.objects.count()
        self.assertNotEqual(old_count, new_count, "If new bucketlist is added counet can't be equal to old")


class ViewTestCase(TestCase):
    """
    Test suite for api views.
    """

    def setUp(self) -> None:
        """Define the test client and other test variables."""
        user = User.objects.create(username="nerd")

        self.client: APIClient = APIClient()
        self.client.force_authenticate(user=user)

        # Since user model instance is not serializable, use its Id/PK
        self.bucketlist_data: dict = {'name': "Go to ibiza", "owner": user.id}

        self.response = self.client.post(
            reverse('create'),
            self.bucketlist_data,
            format="json"
        )

    def test_api_can_create_bucketlist(self) -> None:
        """Test the api has bucket creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_bucketlist(self) -> None:
        """
        Test an api can get a given bucketlist
        """
        bucketlist = Bucketlist.objects.get()

        response = self.client.get(
            reverse('details',
                    kwargs={'pk': bucketlist.id}), format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertContains(response, bucketlist)

    def test_api_can_update_bucketlist(self) -> None:
        """Test the api can update a given bucketlist."""
        bucketlist = Bucketlist.objects.get()
        change_bucketlist: dict = {'name': "Something new"}
        res = self.client.put(
            reverse('details', kwargs={'pk': bucketlist.id}), change_bucketlist, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_bucketlist(self):
        bucketlist = Bucketlist.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': bucketlist.id}),
            format='json',
            follow=True
        )
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
