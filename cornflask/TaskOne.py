class TaskOne:
    def __init__(self):
    
        self.collection_rate = 0
        self.amount_per_parcel = 0
        self.base_pay = 5000
        self.commission_rate = 0

    def validate_successful_delivery(self, collection_rate):

        if collection_rate < 50:
            self.amount_per_parcel = 160
        elif collection_rate < 60:
            self.amount_per_parcel = 200
        elif collection_rate < 70:
            self.amount_per_parcel = 250
        else:
            self.amount_per_parcel = 500

    def calculate_wages(self, collection_rate):
        self.collection_rate = collection_rate
        self.validate_successful_delivery(collection_rate)
        self.commission_rate = (collection_rate * self.amount_per_parcel) + self.base_pay
        return self.commission_rate
