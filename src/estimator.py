def estimator(data):
    output = {'data':data, 'impact': {}, 'severeImpact': {}}
    output['impact']['currentlyInfected'] = data['reportedCases'] * 10
    output['severeImpact']['currentlyInfected'] = data['reportedCases'] * 50
    if data['periodType'] == 'weeks':
        data['timeToElapse'] = data['timeToElapse'] * 7
    elif data['periodType'] == 'months':
        data['timeToElapse'] = data['timeToElapse'] * 30
    output['impact']['infectionsByRequestedTime'] = output['impact']['currentlyInfected'] * (2 ** (data['timeToElapse']//3))
    output['severeImpact']['infectionsByRequestedTime'] = output['severeImpact']['currentlyInfected'] * (2 ** (data['timeToElapse']//3))
    output['impact']['severeCasesByRequestedTime'] = int(15/100 * (output['impact']['infectionsByRequestedTime']))
    output['severeImpact']['severeCasesByRequestedTime'] = int(15/100 * (output['severeImpact']['infectionsByRequestedTime']))
    output['impact']['hospitalBedsByRequestedTime'] = int((35/100 * (data['totalHospitalBeds'])) - output['impact']['severeCasesByRequestedTime'])
    output['severeImpact']['hospitalBedsByRequestedTime'] = int((35/100 * (data['totalHospitalBeds'])) - output['severeImpact']['severeCasesByRequestedTime'])
    output['impact']['casesForICUByRequestedTime'] = int(5/100 * output['impact']['infectionsByRequestedTime'])
    output['severeImpact']['casesForICUByRequestedTime'] = int(5/100 * output['severeImpact']['infectionsByRequestedTime'])
    output['impact']['casesForVentilatorsByRequestedTime'] = int(2/100 * output['impact']['infectionsByRequestedTime'])
    output['severeImpact']['casesForVentilatorsByRequestedTime'] = int(2/100 * output['severeImpact']['infectionsByRequestedTime'])
    output['impact']['dollarsInFlight'] = int((output['impact']['infectionsByRequestedTime'] * data['region']['avgDailyIncomeInUSD'] * data['region']['avgDailyIncomePopulation']) /data['timeToElapse'])
    output['severeImpact']['dollarsInFlight'] = int((output['severeImpact']['infectionsByRequestedTime'] * data['region']['avgDailyIncomeInUSD'] * data['region']['avgDailyIncomePopulation'])/data['timeToElapse'])
    return output

if __name__ == "__main__":
    data = {
      'region':{
        'name':'Africa', 
        'avgAge':19.7, 
        'avgDailyIncomeInUSD':5, 
        'avgDailyIncomePopulation':0.71
      },
        'periodType':'days', 
        'timeToElapse':58, 
        'reportedCases':674, 
        'population':66622705, 
        'totalHospitalBeds':1380614
    }
    dic = estimator(data)
    print(dic)

    data2 = {
      'region':{
        'name':'Africa', 
        'avgAge':19.7, 
        'avgDailyIncomeInUSD':4, 
        'avgDailyIncomePopulation':0.73
      },
        'periodType':'days', 
        'timeToElapse':38, 
        'reportedCases':2747, 
        'population':92931687, 
        'totalHospitalBeds':678874
    }
    dic2 = estimator(data2)
    print(dic2)
