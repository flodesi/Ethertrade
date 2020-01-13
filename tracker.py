import trackingmore
from datetime import date, time, datetime

class tracker:

    tracking_number = None
    carrier = None

    def __init__(self):
        trackingmore.set_api_key('668916b2-77ff-45e7-9eb9-0b035f8e11d6')
        now = datetime(1999, 1, 1)
        self.contract_creation = (now.strftime("%Y"), now.strftime("%m"), now.strftime("%d"))

    def get_shipping_history(self):
        if self.carrier and self.tracking_number:
            tracking = trackingmore.get_tracking_item(self.carrier, self.tracking_number)
            return tracking
        return None

    def validity_check(self, info) -> bool:
        year = info['origin_info']['ItemReceived'][0:4]
        month = info['origin_info']['ItemReceived'][5:7]
        day = info['origin_info']['ItemReceived'][8:10]
        if year >= self.contract_creation[0] and month >= self.contract_creation[1] and day >= self.contract_creation[2]:
            return True
        return False


    def is_valid(self) -> bool:
        info = self.get_shipping_history()
        if info:
            return self.validity_check(info)
        return False

    def set_tracking_number(self, tracking) -> None:
        self.tracking_number = tracking

    def set_carrier(self, carrier) -> None:
        self.carrier = carrier

    def get_tracking_number(self) -> str:
        return self.tracking_number

if __name__ == "__main__":
    print('hello world')
