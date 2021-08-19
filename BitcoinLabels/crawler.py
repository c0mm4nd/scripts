import re
import sys
import time
import urllib.request
import urllib.error
# import redis

base_url = 'https://www.walletexplorer.com'


def urlopen(url):
    delay = 10
    while True:
        try:
            res = urllib.request.urlopen(url)
            return res
        except (urllib.error.HTTPError, urllib.error.URLError) as e:
            print(e)
            print("retrying after " + str(delay) + "s")
            time.sleep(delay)
            delay *= 2


def fetch_addrs(owner, addr_page):
    out = open("addrs_"+owner+".csv", "w+")
    def write_addr_label(label, addrs):
        for addr in addrs:
            out.write(addr+ " " + label + "\n")
    cur_page_num = 1
    total_page_num = 1
    time.sleep(10)
    print("starting "+ owner)
    with urlopen(addr_page) as response:
        raw = response.read()
        encoding = response.headers.get_content_charset('utf-8')
        html = raw.decode(encoding)
        results = re.findall(r'page=([0-9]+)">Last', html)
        total_page_num = int(results[0])
        
        addrs = re.findall(r'href=[\'"]?/address/([^\'" >]+)', html)
        write_addr_label(owner, addrs)
        print(owner+ ": 1/" + str(total_page_num))
    
    while cur_page_num < total_page_num:
        cur_page_num += 1 
        time.sleep(10)
        with urlopen(addr_page + "?page=" + str(cur_page_num)) as response:
            addrs = re.findall(r'href=[\'"]?/address/([^\'" >]+)', html)
            write_addr_label(owner, addrs)
            print(owner+ ": "+ str(cur_page_num) + "/" + str(total_page_num))

    pass


def main():
    # db = redis.Redis(host='localhost', port=6379, db=0)
    # first step, download all entity urls from https://www.walletexplorer.com/
    with urlopen(base_url) as response:
        raw = response.read()
        encoding = response.headers.get_content_charset('utf-8')
        html = raw.decode(encoding)
        results = re.findall(r'href=[\'"]?/wallet/([^\'" >]+)', html)
        
        print("got address owners: ")
        print(dict(enumerate(results)))

        arg_num = len(sys.argv) - 1
        if arg_num == 0:
            id = input("input the owner id, if empty crawler will fetch ALL owners: ")
            if len(id) == 0:
                for owner in results:
                    fetch_addrs(owner, base_url+"/wallet/"+owner+"/addresses")
            else:
                owner = results[int(id)]
                fetch_addrs(owner, base_url+"/wallet/"+owner+"/addresses")
        else:
            try:
                id = sys.argv[1]
                owner = results[int(id)]
                fetch_addrs(owner, base_url+"/wallet/"+owner+"/addresses")
            except:
                if sys.argv in results:
                    fetch_addrs(sys.argv, base_url+"/wallet/"+owner+"/addresses")
                else:
                    print("invalid args")
                    print(sys.argv)
                    exit(0)


if __name__ == "__main__":
    main()
