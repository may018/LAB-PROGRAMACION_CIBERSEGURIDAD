import shodan
import time
import json
import sys



SHODAN_API_KEY = "YOUR_API_KEY"
api = shodan.Shodan(SHODAN_API_KEY)


def show_time(t):
    if t < 60:
        return str(t) + 's'
    if t < 3600:
        return str(t / 60) + 'm:' + str(t % 60) + 's'
    else:
        return str(t / 3600) + 'h:' + str(t % 3600 / 60) + 'm:' + str(t % 3600 % 60) + 's'



def getShodan():

    query = raw_input('Que quieres buscar: ')
    filename = raw_input('Nombre para el archivo donde se guardaran los datos : ')

    starttime = time.time()                 

    results = api.search(query)             
    total = results['total']                

    num = total / 100 + 1                 

    print 'Total de resultados %d , páginas : %d' % (total, num)
    file1 = filename + '.txt'               
    file2 = filename + '-full.txt'
    file3 = filename + '-all.txt'
    fp1 = open(file1, 'w+')               
    fp2 = open(file2, 'w+')
    fp3 = open(file3, 'w+')

    for i in range(1, num, 1):
        try:
            results = api.search(query, page=i)                
            endtime = time.time()                           
            print 'página %d time: %s ' % (i, num - i, show_time(int(endtime - starttime)))
            for result in results['matches']:                  
                fp1.write(result['ip_str'] + ' | ' + str(result['port']) + '\n')

        
                fp2.write(result['ip_str'] + ' | ' + str(result['port']) + ' | ' + result['transport'] + ' | ' +
                          str(result['hostnames']) + ' | ' + str(result['domains']) + ' | ' +
                          str(result['location']['country_name']) + ' | ' +
                          str(result['location']['city']) + ' | ' +
                          str(result['location']['longitude']) + ' | ' +
                          str(result['location']['latitude']) + '\n')

                data = {

                    "ip_str": result['ip_str'],

                    "port": result['port'],
                    "timestamp": result['timestamp'],
                    "hostnames": [
                        result['hostnames']
                    ],
                    "domains": [
                        result['domains']
                    ],
                    "location": {
                        "city": result['location']['city'],
                        "country_code": result['location']['country_code'],
                        "country_code3": result['location']['country_code3'],
                        "country_name": result['location']['country_name'],
                        "dma_code": result['location']['dma_code'],

                        "latitude": result['location']['latitude'],
                        "longitude": result['location']['longitude'],
                        "postal_code": result['location']['postal_code'],
                        "region_code": result['location']['region_code']
                    },
                    "org": result['org'],
                    "isp": result['isp'],
                    "os": result['os'],
                    "transport": result['transport'],

                }

                data_str = json.dumps(data)
 
                json.dump(data, fp3)
                fp3.write('\n')

     
        except shodan.APIError, e:
            print 'Error: %s' % e
            continue

 
    endtime = time.time()
    print 'Esto consume mucho tiempo : %s s' % show_time(int(endtime - starttime))
    fp1.close()           
    fp2.close()
    fp3.close()



if __name__ == '__main__':
    getShodan()

