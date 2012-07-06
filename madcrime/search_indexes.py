import datetime
from haystack import indexes
from madcrime.models import Incident

class IncidentIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    typeDetails = indexes.CharField(model_attr='typeDetails')
    dateDetails = indexes.DateTimeField(model_attr='dateDetails')
    linkIncidents = indexes.CharField(model_attr='linkIncidents')
    detailsDetails = indexes.CharField(model_attr='detailsDetails')

    def get_model(self):
        return Incident

    def index_queryset(self):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(dateIncidents__lte=datetime.datetime.now()).order_by('-dateDetails', 'typeDetails')
        
        