#https://leetcode.com/discuss/interview-question/1487965/Twitter-Coding-Question-Vacate-hosts-in-Rack

"""
build rack_map dictionary

"<rack_id>": {
    "services" = set('timelines', 'tweets')    # services in the rack
    "total_hosts": 3           # total hosts in a rack
    "service_host_count": 2    # host count for selected service
    "service_hosts": []        # list of hosts for selected service 
}
"""

import os;
def vacate(service, replacement_count, hostname_service_lists):
    rack_map = {} # service and other services
    
    service_racks = []
    print(hostname_service_lists)
    hostname_service_list=hostname_service_lists.split('\n')
    for item in hostname_service_list:
        print(item)
        splitted = item.split()
        print(splitted)
        r = splitted[0].split('-')
        rack=r[0]
        app = splitted[-1]
        hostname = splitted[0]
        
        if rack in rack_map:
            if app !='empty':
                rack_map[rack]['services'].add(app)
                rack_map[rack]["total_hosts"] += 1
            if app == service:
                rack_map[rack]['service_host_count'] += 1
                rack_map[rack]['service_hosts'].append(hostname)
        else:
            if app == service:
                rack_map[rack] = {"services":{app}, "total_hosts": 1, "service_host_count": 1, 'service_hosts': [hostname]}
            else:
                rack_map[rack] = {"services":{app}, "total_hosts": 1, "service_host_count": 0, 'service_hosts': []}


    service_ordered_rack = sorted(rack_map.items(), key=lambda x: (len(x[1]['services']),len(x[1]['service_hosts'])))
    
    print("=============================================rackmap populated now ========================")
    print("RACKMAP:",rack_map)
    print("---------------------------------------------------------")
    print("Sorted :",service_ordered_rack)
    print("============================================================ ========================")
    ans = []
    c = 0
    for item in service_ordered_rack:
        if item[1]['service_host_count'] == 0:
            continue
        #if len(rack_map[rack]['services']) == 1 and service in rack_map[rack]['services']:
        if len(item[1]['services']) == 1 and service in item[1]['services']:
            print("Inside If while")
            while c < replacement_count and item[1]['service_hosts']:
                print("Inside WHILE")
                host = item[1]['service_hosts'].pop()
                ans.append(host)
                c+=1
        if c>=replacement_count:
            break
    if c>=replacement_count:
        return ans
    else:
        print(ans)
        return "[can not possible]"

    

hostname_service_list='''aaa-01.prod.twttr.net timelines
aaa-02.prod.twttr.net empty
aaa-03.prod.twttr.net empty
aab-01.prod.twttr.net timelines
aab-02.prod.twttr.net timelines
aab-03.prod.twttr.net empty
aac-01.prod.twttr.net timelines
aac-02.prod.twttr.net empty
aac-03.prod.twttr.net tweets
aad-01.prod.twttr.net timelines
aad-02.prod.twttr.net empty
aad-03.prod.twttr.net empty'''
result = vacate('timelines',2, hostname_service_list)
print(result)

