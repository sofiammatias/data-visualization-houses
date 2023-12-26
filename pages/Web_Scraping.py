import streamlit as st
import requests
import pandas as pd
import json
import os
import re
from bs4 import BeautifulSoup  # type :ignore
from dotenv import load_dotenv

# get url as environment var
load_dotenv()
url = os.environ.get('URL')

# Fill page with info
st.set_page_config(page_title="Web Scraping Data", page_icon="📋")

st.title("Houses for Sale for loft.br")
st.subheader("Jardim América, São Paulo, Brasil")
st.markdown ("""
This app shows a small demo of data taken by web scraping of a brazilian estate website (loft.br)
and some data visualization about the data retrieved. \nIn this page, you can run web scraping and 
retrieve updated information from the website. Save the data in csv, then load the file in the page
"Data Visualization With Streamlit" and you can see the graphics with updated data.
""")
st.write(f"Web scraping URL: {url}")


def website_scraped(soup, state: bool, url: str, counter:int, num_pages:int):
    """
        Scrapes website from page "counter" to page "num_pages".
        Retrieves house url, house type, house price, lat, long, address, number of bedrooms, 
        parking space.
        Retrieves lat and long from each house url.
        REtrieves the rest of info from the current page.   
    """

    
    def json_extract(obj, key):
        """Extract nested values from a JSON tree: recursively fetch values from nested JSON."""
        arr = []

        def extract(obj, arr, key):
            """Recursively search for values of key in JSON tree."""
            if isinstance(obj, dict):
                for k, v in obj.items():
                    if isinstance(v, (dict, list)):
                        extract(v, arr, key)
                    elif k == key:
                        arr.append(v)
            elif isinstance(obj, list):
                for item in obj:
                    extract(item, arr, key)
            return arr

        values = extract(obj, arr, key)
        return values

    info_to_df = []
    payload = {}
    progress_text = f"Scraping website page {counter} of {num_pages}"
    my_bar = st.progress(0, text=progress_text)
    for i in range(counter, num_pages):
        contents = soup.find_all("div", {"class": "MuiGrid-root jss125 MuiGrid-item MuiGrid-grid-xs-12 MuiGrid-grid-sm-6 MuiGrid-grid-md-3 MuiGrid-grid-lg-3"})
        for j, content in enumerate(contents):
            my_bar.progress(int(100 * j / len(contents)), text=progress_text)
            content_text = content.text
            regex = r"(.*?)R\$ ([\d.,]+)(.*?)m²(\d+)m²?(\d+)"
            matches = re.match(regex, content_text)
            if matches is not None:
                result = [matches.group(i).strip() for i in range(1, 6)]
            new_partial_link = content.find("a", {"class": "MuiButtonBase-root MuiCardActionArea-root jss266"}).get("href")
            new_link = f"https://loft.com.br{new_partial_link}"
            response = requests.get(new_link)
            soup = BeautifulSoup(response.text, "html.parser")
            json_info = json.loads(soup.find("script",{"type":"application/json"}).text)

            latitude = float(json_extract(json_info, "latitude")[0])
            longitude = float(json_extract(json_info, "longitude")[0])
            
            info_to_df.append(
                dict(
                    house_links=new_link,
                    house_type=result[0],
                    house_price=int(result[1].replace(".", "")),
                    address=result[2],
                    area=result[3],
                    bedrooms=result[4][0],
                    parking_space=result[4][1],
                    latitude=latitude,
                    longitude=longitude,
                )
            )

        payload["pagina"] = i+1
        progress_text = f"Scraping website page {i+1} of {num_pages}"
        response = requests.get(url, params=payload)
        soup = BeautifulSoup(response.text, "html.parser")
        if "Nenhum imóvel encontrado" in soup.text or state == True:
            break
    houses_df = pd.DataFrame(info_to_df)
    return houses_df

# initialize scraping loop
houses_df = pd.DataFrame([])
i = 0
col1, col2 = st.columns([3,1])

# buttons for web scraping and cancel web scraping
with col1:
    if st.button("Scrape Website"):
        st.session_state['webscraping'] = True
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        pages = soup.find("a", {"class": "MuiTypography-root MuiLink-root jss349 MuiLink-underlineNone jss350 jss365 jss352 jss367 jss342 MuiTypography-colorPrimary"})
        num_pages = int(pages.getText())

        while st.session_state['webscraping'] == True or i != num_pages:
            partial_houses_df = website_scraped(soup, st.session_state['webscraping'], url, i, num_pages)
            i += 1
        houses_df = pd.concat ([houses_df, partial_houses_df]) 
with col2:
    if st.button("Cancel Scraping"):
        st.session_state['webscraping'] = False

if st.session_state['webscraping'] == False or i == num_pages:
    # Save file        
    houses_df.to_csv("houses.csv", index=False)
    st.success(
              'File "houses.csv" is ready to be saved. Use the button below to save file locally.'
            )

    @st.cache_data
    def convert_df(df):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return df.to_csv().encode("utf-8")

    csv = convert_df(houses_df)

    st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name="houses_df.csv",
        mime="text/csv",
    )

    st.header("Downloaded data")
    st.dataframe(houses_df)


#if __name__ == '__main__':
#    print (url)
#    result = website_scraped(url)
#    print(result)
#    with open("C:\\Users\\xufia\\OneDrive\\Ambiente de Trabalho\\result.txt", "w", encoding="utf-8") as file:
#        file.write(str(result))

