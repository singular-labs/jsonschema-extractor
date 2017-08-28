from .extractor_set import SchemaExtractorSet

from .typing_extractor import TypingExtractor
from .attrs_extractor import AttrsExtractor
DEFAULT_EXTRACTOR_LIST = [
    AttrsExtractor(),
    TypingExtractor()
]
# if schematics exists, then we import this
try:
    from .schematics_extractor import SchematicsExtractor
    DEFAULT_EXTRACTOR_LIST.insert(0, SchematicsExtractor())
except ImportError:
    pass

def extract_jsonschema(typ):
    return DEFAULT_EXTRACTOR.extract(typ)

def init_default_extractor():
    """
    create a new extractor, providing the default (all available
    extractors)
    """
    return SchemaExtractorSet(DEFAULT_EXTRACTOR_LIST)

DEFAULT_EXTRACTOR = init_default_extractor()
