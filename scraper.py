import requests
import pandas as pd
import base64

def decode(l):
    try:
        return base64.b85decode(l).decode("utf-8").split(" ")[0]
    except:
        return l

def main():
    # URL of the website
    url = "https://movitv.pro/"

    # Send a GET request to the URL
    response = requests.get(url)
    urls = response.text.split("\n")[2:]

    # add all the items to a dataframe
    df = pd.DataFrame(urls, columns=["url"])

    forbidden_strings = ['', ' ']
    # Removing rows that contain any of the forbidden strings
    for forbidden_string in forbidden_strings:
        df = df[df['url'] != forbidden_string].reset_index(drop=True)

    # Split the DataFrame into titles and links
    # Titles are now in the even index rows (0, 2, 4, ...) and links in the odd index rows (1, 3, 5, ...)
    titles = df.iloc[::2].reset_index(drop=True)
    links = df.iloc[1::2].reset_index(drop=True)

    # Combine the two DataFrames
    df = pd.concat([titles, links], axis=1)
    df.columns = ['Title', 'Link']

    # split df["Title"] by comma and get the last element
    df["Title"] = df["Title"].str.split(",").str[-1]

    df["Link"] = df["Link"].apply(decode)

    df = df.dropna().reset_index(drop=True)

    df.to_csv("links.csv", index=False)

if __name__ == "__main__":
    main()