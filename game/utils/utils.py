class Utils:
    
    min_index = None
    max_index = None
    
    @staticmethod
    def set_indexes(min_index, max_index):
        Utils.min_index = min_index
        Utils.max_index = max_index
    
    @staticmethod
    def get_indexes():
        return Utils.min_index, Utils.max_index