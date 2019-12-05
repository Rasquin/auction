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
        artifact = Artifact(name="A name", origin="A culture", year=500, description="A description", crafting="How was the artifact made", trajectory="Interesting events regarding this artifact", expert_value=10, minimun_bidding_price=2.50, current_bidding_price=5.00, buy_now_price=5.00, price_to_pay=5.00, published_date=timezone.now, end_date=timezone.now, on_bidding=True)
        self.assertEqual(artifact.name, "A name")
        self.assertEqual(artifact.origin, "A culture")
        self.assertEqual(artifact.year, 500)
        self.assertEqual(artifact.description, "A description")
        self.assertEqual(artifact.crafting, "How was the artifact made")
        self.assertEqual(artifact.trajectory, "Interesting events regarding this artifact")
        self.assertEqual(artifact.expert_value, 10.00)
        self.assertEqual(artifact.minimun_bidding_price, 2.50)
        self.assertEqual(artifact.current_bidding_price, 5.00)
        self.assertEqual(artifact.buy_now_price, 5.00)
        self.assertEqual(artifact.price_to_pay, 5.00)
        self.assertEqual(artifact.published_date, timezone.now)
        self.assertEqual(artifact.end_date, timezone.now)
        self.assertTrue(artifact.on_bidding)
        
    

    def test_str(self):
        artifact = Artifact(name="A name", origin="A culture", description="A description", crafting="How was the artifact made", trajectory="Interesting events regarding this artifact" )
        self.assertEqual(str(artifact.name), "A name")
        self.assertEqual(str(artifact.origin), "A culture")
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