from api.serializers import (TagSetDetailSerializer, FeatureDetailSerializer, 
                             DimensionSerializer)
from wordDictionary.models import TagSet, Feature, Dimension


# Returns all the possible features for
# the word's dimension in following format:
# { 'dim1': [['feat1', True], ['feat2', False], ...], ... }

def getDimOptions(tagset):
    # result is returned as a dictionary
    result = {}
    dim = DimensionSerializer(Dimension.objects.all(), many=True)
    feat = FeatureDetailSerializer(Feature.objects.all(), many=True)
    # stores all unique dimensions that are possible in a language
    tag_names = set([])
    # stores all feature names of a ward
    feat_names = []
    for i in tagset['features']:
        feat_names.append(i['name'])
        tag_names.add(i['dimension']['name'])
    for i in tag_names:
        result[i] = []
    for f in feat.data:
        for d in dim.data:
            if(f['dimension']['id'] == d['id'] and d['name'] in tag_names):
                if(f['name'] in feat_names):
                    result[d['name']].append([f['name'], True])
                result[d['name']].append([f['name'], False])
    return result
