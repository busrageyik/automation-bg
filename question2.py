class WebPush:
    def __init__(self, platform, optin,global_frequency_capping, start_date, end_date, language, push_type):
        self.platform=platform
        self.obtin=optin
        self.global_frequency_capping=global_frequency_capping
        self.start_date=start_date
        self.end_date=end_date
        self.language=language
        self.push_type=push_type

   def send_push():
       print ("Push has been sent to the user!")
class TriggerPush(WebPush):
    string trigger_page
class BulkPush(WebPush):
    integer send_date
class SegmentPush(WebPush):
    string segment_name
class PriceAlertPush(WebPush):
    integer price_info
    float discount_rate
    discountPrice(price_info, discount_rate)
class InStockPush(WebPush):
    def stockUpdate(self, stock_info):
        if (stock_info == True):
            stock_info == False
        else:
            stock_info == True


    return stock_info

instock = InstockPush('Desktop', True, 0, 1607879442, 1607879475, 'Poland', 'In Stock Push', False)
instock.stockUpdate(True)
instock.send_push()
