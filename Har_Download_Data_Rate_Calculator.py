import sys
import json

def sum_size_fields(contents):
    har_data = json.loads(contents)

    total_size = 0
    for entry in har_data['log']['entries']:
        size = entry['response']['content']['size']
        if isinstance(size, int):
            total_size += size
    
    return total_size

def find_onLoad(contents):
    har_data = json.loads(contents)
    onload = 0
    for page in har_data['log']['pages']:
        if 'pageTimings' in page and 'onLoad' in page['pageTimings']:
            onload = (page['pageTimings']['onLoad'])

    return onload

def main():    

    fname = sys.argv[1]

    file = open(fname, 'r')
    contents = file.read()

    print(find_onLoad(contents))
    print("Download data rate is:", (sum_size_fields(contents)/find_onLoad(contents))/(1000),"Mbps")

    file.close()

if __name__ == "__main__":
    main()
