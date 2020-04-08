from bearerauth import BearerAuth, requests
import constants
import build_query


def vectronics_api_calls():
    try:
        device_gps_data = requests.get(
            constants.VECTRONICS_URL+'/1000001/gps?collarkey=6484B8CA88E2B996421AB903D0B215AFAE285CAAE932F35F448154398398CF33AC40D37D9E37CEEA9DFCBD89353C3CCF8628A4DB4523F2324A83ADA5D091FB396DAC72773ED8CE1571D5C254FABBA0FBDEE2E1883694B8D18148168B205ED5BFA96ACEC30B7B99E045B8AE145B2A83948BAECD54CAB80A7676360B74CD1DEF7DDB50293E36B1C900EA853E19F808F745D85610F68609F233E294FA1C84700A80F1C257E062CAF4B2467E518A010A59E636091BAB905E50ED300BADF9F90440F7B85BBE14DD864BBB2F77A0A50BE5E14623D1B8FB0C2A3069207F4BFBF6CFEBC152F072D27B3CE88F844ED0197A56AF5114DE7B3BA544DB880850507FEB046684')
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    try:
        device_activity_data = requests.get(
            constants.VECTRONICS_URL+'/1000001/act?collarkey=6484B8CA88E2B996421AB903D0B215AFAE285CAAE932F35F448154398398CF33AC40D37D9E37CEEA9DFCBD89353C3CCF8628A4DB4523F2324A83ADA5D091FB396DAC72773ED8CE1571D5C254FABBA0FBDEE2E1883694B8D18148168B205ED5BFA96ACEC30B7B99E045B8AE145B2A83948BAECD54CAB80A7676360B74CD1DEF7DDB50293E36B1C900EA853E19F808F745D85610F68609F233E294FA1C84700A80F1C257E062CAF4B2467E518A010A59E636091BAB905E50ED300BADF9F90440F7B85BBE14DD864BBB2F77A0A50BE5E14623D1B8FB0C2A3069207F4BFBF6CFEBC152F072D27B3CE88F844ED0197A56AF5114DE7B3BA544DB880850507FEB046684')
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    try:
        device_proximity_data = requests.get(
            constants.VECTRONICS_URL+'/1000001/prx?collarkey=6484B8CA88E2B996421AB903D0B215AFAE285CAAE932F35F448154398398CF33AC40D37D9E37CEEA9DFCBD89353C3CCF8628A4DB4523F2324A83ADA5D091FB396DAC72773ED8CE1571D5C254FABBA0FBDEE2E1883694B8D18148168B205ED5BFA96ACEC30B7B99E045B8AE145B2A83948BAECD54CAB80A7676360B74CD1DEF7DDB50293E36B1C900EA853E19F808F745D85610F68609F233E294FA1C84700A80F1C257E062CAF4B2467E518A010A59E636091BAB905E50ED300BADF9F90440F7B85BBE14DD864BBB2F77A0A50BE5E14623D1B8FB0C2A3069207F4BFBF6CFEBC152F072D27B3CE88F844ED0197A56AF5114DE7B3BA544DB880850507FEB046684')
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    try:
        device_separation_data = requests.get(
            constants.VECTRONICS_URL+'/1000001/sep?collarkey=6484B8CA88E2B996421AB903D0B215AFAE285CAAE932F35F448154398398CF33AC40D37D9E37CEEA9DFCBD89353C3CCF8628A4DB4523F2324A83ADA5D091FB396DAC72773ED8CE1571D5C254FABBA0FBDEE2E1883694B8D18148168B205ED5BFA96ACEC30B7B99E045B8AE145B2A83948BAECD54CAB80A7676360B74CD1DEF7DDB50293E36B1C900EA853E19F808F745D85610F68609F233E294FA1C84700A80F1C257E062CAF4B2467E518A010A59E636091BAB905E50ED300BADF9F90440F7B85BBE14DD864BBB2F77A0A50BE5E14623D1B8FB0C2A3069207F4BFBF6CFEBC152F072D27B3CE88F844ED0197A56AF5114DE7B3BA544DB880850507FEB046684')
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    try:
        device_vaginal_implant_data = requests.get(
            constants.VECTRONICS_URL+'/1000001/vit?collarkey=6484B8CA88E2B996421AB903D0B215AFAE285CAAE932F35F448154398398CF33AC40D37D9E37CEEA9DFCBD89353C3CCF8628A4DB4523F2324A83ADA5D091FB396DAC72773ED8CE1571D5C254FABBA0FBDEE2E1883694B8D18148168B205ED5BFA96ACEC30B7B99E045B8AE145B2A83948BAECD54CAB80A7676360B74CD1DEF7DDB50293E36B1C900EA853E19F808F745D85610F68609F233E294FA1C84700A80F1C257E062CAF4B2467E518A010A59E636091BAB905E50ED300BADF9F90440F7B85BBE14DD864BBB2F77A0A50BE5E14623D1B8FB0C2A3069207F4BFBF6CFEBC152F072D27B3CE88F844ED0197A56AF5114DE7B3BA544DB880850507FEB046684')
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    try:
        device_mortality_data = requests.get(
            constants.VECTRONICS_URL+'/1000001/mor?collarkey=6484B8CA88E2B996421AB903D0B215AFAE285CAAE932F35F448154398398CF33AC40D37D9E37CEEA9DFCBD89353C3CCF8628A4DB4523F2324A83ADA5D091FB396DAC72773ED8CE1571D5C254FABBA0FBDEE2E1883694B8D18148168B205ED5BFA96ACEC30B7B99E045B8AE145B2A83948BAECD54CAB80A7676360B74CD1DEF7DDB50293E36B1C900EA853E19F808F745D85610F68609F233E294FA1C84700A80F1C257E062CAF4B2467E518A010A59E636091BAB905E50ED300BADF9F90440F7B85BBE14DD864BBB2F77A0A50BE5E14623D1B8FB0C2A3069207F4BFBF6CFEBC152F072D27B3CE88F844ED0197A56AF5114DE7B3BA544DB880850507FEB046684')
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    try:
        device_mortality_implant_data = requests.get(
            constants.VECTRONICS_URL+'/1000001/mit?collarkey=6484B8CA88E2B996421AB903D0B215AFAE285CAAE932F35F448154398398CF33AC40D37D9E37CEEA9DFCBD89353C3CCF8628A4DB4523F2324A83ADA5D091FB396DAC72773ED8CE1571D5C254FABBA0FBDEE2E1883694B8D18148168B205ED5BFA96ACEC30B7B99E045B8AE145B2A83948BAECD54CAB80A7676360B74CD1DEF7DDB50293E36B1C900EA853E19F808F745D85610F68609F233E294FA1C84700A80F1C257E062CAF4B2467E518A010A59E636091BAB905E50ED300BADF9F90440F7B85BBE14DD864BBB2F77A0A50BE5E14623D1B8FB0C2A3069207F4BFBF6CFEBC152F072D27B3CE88F844ED0197A56AF5114DE7B3BA544DB880850507FEB046684')
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    device_gps_data_dict = device_gps_data.json()
    device_activity_data_dict = device_activity_data.json()
    device_proximity_data_dict = device_proximity_data.json()
    device_separation_data_dict = device_separation_data.json()
    device_vaginal_implant_data_dict = device_vaginal_implant_data.json()
    device_mortality_data_dict = device_mortality_data.json()
    device_mortality_implant_data_dict = device_mortality_implant_data.json()

    a = [["api_gpsplusx_device_gps_data", device_gps_data_dict],
         ["api_gpsplusx_device_activity_data", device_activity_data_dict],
         ["api_gpsplusx_device_proximity_data", device_proximity_data_dict],
         ["api_gpsplusx_device_separation_data", device_separation_data_dict],
         ["api_gpsplusx_device_vaginal_implant_data", device_vaginal_implant_data_dict],
         ["api_gpsplusx_device_mortality_data", device_mortality_data_dict],
         ["api_gpsplusx_device_mortality_implant_data", device_mortality_implant_data_dict]]

    for i in range(len(a)):
        table_name = a[i][0]
        info_dict = a[i][1]

        build_query.build_query(table_name, info_dict)

    return
