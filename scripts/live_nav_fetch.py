import requests
import pandas as pd
from pathlib import Path
import time

OUTPUT_DIR = Path("./data/raw")

schemes = {
    "HDFC_Top_100":125497,
    "SBI_Bluechip":119551,
    "ICICI_Bluechip":120503,
    "Nippon_Large_Cap":118632,
    "Axis_Bluechip":119092,
    "Kotak_Bluechip":120841
}

for scheme_name, scheme_code in schemes.items():

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    print(f"\nFetching {scheme_name}")

    try:

        response = requests.get(
            url,
            headers={
                "User-Agent":
                "Mozilla/5.0"
            },
            timeout=30
        )

        print(
            "Status:",
            response.status_code
        )

        if response.status_code != 200:

            print(
                "Request failed"
            )

            continue

        try:

            data = response.json()

        except Exception:

            print(
                "JSON parsing failed"
            )

            print(
                response.text[:300]
            )

            continue

        if "data" not in data:

            print(
                "No NAV data found"
            )

            continue

        nav_df = pd.DataFrame(
            data["data"]
        )

        output_file = (
            OUTPUT_DIR /
            f"{scheme_name}_live_nav.csv"
        )

        nav_df.to_csv(
            output_file,
            index=False
        )

        print(
            f"Saved: {output_file}"
        )

        time.sleep(2)

    except Exception as e:

        print(
            f"Error: {e}"
        )



# import requests
# import pandas as pd
# from pathlib import Path

# OUTPUT_DIR = Path("./data/raw")

# schemes = {
#     "HDFC_Top_100": 125497,
#     "SBI_Bluechip": 119551,
#     "ICICI_Bluechip": 120503,
#     "Nippon_Large_Cap": 118632,
#     "Axis_Bluechip": 119092,
#     "Kotak_Bluechip": 120841
# }

# for scheme_name, scheme_code in schemes.items():

#     print(f"Fetching {scheme_name}")

#     url = f"https://api.mfapi.in/mf/{scheme_code}"

#     try:

#         # response = requests.get(url)
#         response = requests.get(
#         url,
#         headers={
#             "User-Agent":
#             "Mozilla/5.0"
#         },
#         timeout=30
#         )

#         data = response.json()

#         nav_df = pd.DataFrame(data["data"])

#         output_file = (
#             OUTPUT_DIR /
#             f"{scheme_name}_live_nav.csv"
#         )

#         nav_df.to_csv(
#             output_file,
#             index=False
#         )

#         print(
#             f"Saved: {output_file}"
#         )

#     except Exception as e:

#         print(
#             f"Error fetching {scheme_name}"
#         )

#         print(e)

# print("\nFinished.")