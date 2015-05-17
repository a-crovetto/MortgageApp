from chartit import DataPool, Chart

ds = DataPool(
       series=
        [{'options': {
            'source': },
          'terms': [
            'month',
            'houston_temp', 
            'boston_temp']}
         ])

cht = Chart(
        datasource = ds, 
        series_options = 
          [{'options':{
              'type': 'line',
              'stacking': False},
            'terms':{
              'month': [
                'boston_temp',
                'houston_temp']
              }}],
        chart_options = 
          {'title': {
               'text': 'Weather Data of Boston and Houston'},
           'xAxis': {
                'title': {
                   'text': 'Month number'}}})