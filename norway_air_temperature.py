import scrapy


class NorwayAirTemperatureSpider(scrapy.Spider):
    name = 'norway_air_temperature'
    allowed_domains = ['https://thredds.met.no/thredds/dodsC/mepslatest/meps_lagged_6_h_latest_2_5km_latest.nc.html']
    start_urls = ['http://https://thredds.met.no/thredds/dodsC/mepslatest/meps_lagged_6_h_latest_2_5km_latest.nc.html/']

    def parse(self, response):
        param = "air_temperature_2m"
        for i in response.css(param):
            pass
        <^>NAME_SELECTOR = 'Float32 a ::text'
            yield {
                'name': i.css(NAME_SELECTOR).extract_first(),
            }<^>




#Grid {
#     ARRAY:
#        Float32 air_temperature_2m[time = 62][height0 = 1][ensemble_member = 30][y = 1069][x = 949];
#     MAPS:
#        Float64 time[time = 62];
#        Float32 height0[height0 = 1];
#        Int16 ensemble_member[ensemble_member = 30];
#        Float32 y[y = 1069];
#        Float32 x[x = 949];
#    } air_temperature_2m;
#    Grid {