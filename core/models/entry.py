from core.models_bases import load_model_class
from core.setting import ENTRY_BASIC_MODEL


class Entry(load_model_class(ENTRY_BASIC_MODEL)):
    """
    The Entry model based on inheritence
    """