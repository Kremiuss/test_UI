# Alexandr_Shelkovich Test_UI

INSTALLATION:

pip install -r requirements.txt

TEST RUN SEQUENCE:
1) pytest -v -s -m phones_page --reruns 2 --alluredir reports
2) pytest -v -s -m selected_phone_page --reruns 2 --alluredir reports
3) allure serve reports