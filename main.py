import requests
import random
import re

def scrape(newdata):
    yourquery = newdata

    if " " in yourquery:
        yourquery = yourquery.replace(" ", "+")
        url = "https://thehiddenwiki.com/".format(yourquery)
        response = requests.get(url)
        response.raise_for_status()

        content = response.text
        regexquery = "\w+\.onion"
        minedata = re.findall(regexquery, content)

        n = random.randint(1, 9999)
        filename = "sites{}.txt".format(str(n))

        print("Saving to... ", filename)
        minedata = list(dict.fromkeys(minedata))

        for k in minedata:
            with open(filename, "a") as newfile:
                k = k + "\n"
                newfile.write(k)

        print("All the files written to a text file:", filename)

        try:
            with open(filename) as input_file:
                head = [next(input_file) for _ in range(5)]
                contents = '\n'.join(map(str, head))
                print(contents)
        except StopIteration:
            pass

if __name__ == "__main__":
    newdata = input("[*]Please Enter your Query: ")
    scrape(newdata)
