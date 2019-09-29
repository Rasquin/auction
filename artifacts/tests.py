from django.test import TestCase
from .models import Artifact
from django.utils import timezone

# Create your tests here.
class TestArtifactModel(TestCase):
    """
    Here we'll define the tests that we'll run against our
    Artifact model
    """
    
   
    def test_can_create_an_artifact(self):
        artifact = Artifact(name="A name", origin="A culture", age="An age", description="A description", crafting="How was the artifact made", trajectory="Interesting events regarding this artifact", initial_price=100.23, bidding_price=120.45, buying_price=200.00, published_date=timezone.now, bidding_time=200, on_bidding=True)
        self.assertEqual(artifact.name, "A name")
        self.assertEqual(artifact.origin, "A culture")
        self.assertEqual(artifact.age, "An age")
        self.assertEqual(artifact.description, "A description")
        self.assertEqual(artifact.crafting, "How was the artifact made")
        self.assertEqual(artifact.trajectory, "Interesting events regarding this artifact")
        self.assertEqual(artifact.initial_price, 100.23)
        self.assertEqual(artifact.bidding_price, 120.45)
        self.assertEqual(artifact.buying_price, 200.00)
        self.assertEqual(artifact.published_date, timezone.now)
        self.assertEqual(artifact.bidding_time, 200)
        self.assertTrue(artifact.on_bidding)
        
    

    def test_str(self):
        artifact = Artifact(name="A name", origin="A culture", age="An age", description="A description", crafting="How was the artifact made", trajectory="Interesting events regarding this artifact" )
        self.assertEqual(str(artifact.name), "A name")
        self.assertEqual(str(artifact.origin), "A culture")
        self.assertEqual(str(artifact.age), "An age")
        self.assertEqual(str(artifact.description), "A description")
        self.assertEqual(str(artifact.crafting), "How was the artifact made")
        self.assertEqual(str(artifact.trajectory), "Interesting events regarding this artifact")
    

    
        
    """
    def test_artifact_on_biding(self):
        artifact = Artifact(on_bidding=True)
        artifact.save()
        self.assertTrue(artifact.on_bidding)
        

    def test_can_create_an_item_with_a_name_and_status(self):
        item = Item(name="Create a Test", done=True)
        item.save()
        self.assertEqual(item.name, "Create a Test")
        self.assertTrue(item.done)
    """