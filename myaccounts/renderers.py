from rest_framework.renderers import JSONRenderer as BaseJSONRenderer
from .encoders import BaseObjectEncoder


class JSONRenderer(BaseJSONRenderer):
    encoder_class = BaseObjectEncoder
