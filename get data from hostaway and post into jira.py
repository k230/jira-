import requests
import  json
from jira import JIRA
import mysql.connector



jira_username = ''
jira_password = ''
jira_url = ""
jira_secret=''
HA_token = ""
HA_client_secret=''
HA_client_id=''
HA_access_token=''

def pull_HA_push_jira_RD(jira_url,HA_token,HA_client_secret,HA_access_token,jira_secret):

    jira_payload = "{\"fields\": {\"summary\": \"khurram\",\"issuetype\": {\"id\": \"\"},\"project\":{\"id\" : \"\"}}}"


    HA_payload={'grant_type': 'client_credentials',
    'client_id': HA_client_id,
    'client_secret': HA_client_secret,
    'scope': 'general'}




    jira_headers = {
      'Content-Type': 'application/json',
      'Authorization': jira_secret,
      'Cookie': ''
    }

    files = [

    ]

    HA_headers = {
      'Authorization':HA_access_token
    }



    HA_response = requests.request("GET", HA_, headers=HA_headers, data = HA_payload, files = files)
    HA_response=HA_response.text.encode('utf8')

    HA_response = json.loads(HA_response)
    Data=HA_response['result']

    print(Data)

    jira_payload = json.loads(jira_payload)
    print(jira_payload)
    i=0
    for k in Data:
        jira_payload["fields"]["summary"]=str(k["guestName"])+","+str(k["arrivalDate"])+","+str(k["departureDate"])
        print(jira_payload)
        jira_payload['fields']['customfield_10408']= k['reservationId']
        jira_payload['fields']['customfield_10446']= k['adults']
        jira_payload['fields']['customfield_10497']= k['airbnbCancellationPolicy']
        jira_payload['fields']['customfield_10487']= k['airbnbExpectedPayoutAmount']
        jira_payload['fields']['customfield_10488']= k['airbnbListingBasePrice']
        jira_payload['fields']['customfield_10489']= k['airbnbListingCancellationHostFee']
        jira_payload['fields']['customfield_10490']= k['airbnbListingCancellationPayout']
        jira_payload['fields']['customfield_10491']= k['airbnbListingCleaningFee']
        jira_payload['fields']['customfield_10492']= k['airbnbListingHostFee']
        jira_payload['fields']['customfield_10493']= k['airbnbListingSecurityPrice']
        jira_payload['fields']['customfield_10494']= k['airbnbOccupancyTaxAmountPaidToHost']
        jira_payload['fields']['customfield_10495']= k['airbnbTotalPaidAmount']
        jira_payload['fields']['customfield_10496']= k['airbnbTransientOccupancyTaxPaidAmount']
        jira_payload['fields']['customfield_10450']= k['arrivalDate']
        jira_payload['fields']['customfield_10414']= k['assigneeUserId']
        jira_payload['fields']['customfield_10474']= k['braintreeGuestId']
        jira_payload['fields']['customfield_10475']= k['braintreeMessage']
        jira_payload['fields']['customfield_10478']= k['cancellationDate']
        jira_payload['fields']['customfield_10479']= k['cancelledBy']
        jira_payload['fields']['customfield_10469']= k['ccExpirationMonth']
        jira_payload['fields']['customfield_10468']= k['ccExpirationYear']
        jira_payload['fields']['customfield_10466']= k['ccName']
        jira_payload['fields']['customfield_10467']= k['ccNumberEndingDigits']
        jira_payload['fields']['customfield_10461']= k['channelCommissionAmount']
        jira_payload['fields']['customfield_10405']= k['channelId']
        jira_payload['fields']['customfield_10407']= k['channelName']
        jira_payload['fields']['customfield_10410']= k['channelReservationId']
        jira_payload['fields']['customfield_10455']= k['checkInTime']
        jira_payload['fields']['customfield_10456']= k['checkOutTime']
        jira_payload['fields']['customfield_10535']= k['checkOutTime']
        jira_payload['fields']['customfield_10447']= k['children']
        jira_payload['fields']['customfield_10463']= k['cleaningFee']
        jira_payload['fields']['customfield_10546']= k['cleaningFee']
        jira_payload['fields']['customfield_10485']= k['comment']
        jira_payload['fields']['customfield_10486']= k['confirmationCode']
        jira_payload['fields']['customfield_10476']= k['currency']
        jira_payload['fields']['customfield_10501']= k['customFieldValues']
        jira_payload['fields']['customfield_10415']= k['customerIcalId']
        jira_payload['fields']['customfield_10416']= k['customerIcalName']
        jira_payload['fields']['customfield_10470']= k['cvc']
        jira_payload['fields']['customfield_10451']= k['departureDate']
        jira_payload['fields']['customfield_10482']= k['doorCode']
        jira_payload['fields']['customfield_10484']= k['doorCodeInstruction']
        jira_payload['fields']['customfield_10483']= k['doorCodeVendor']
        jira_payload['fields']['customfield_10413']= k['externalUnitId']
        jira_payload['fields']['customfield_10430']= k['guestAddress']
        jira_payload['fields']['customfield_10417']= k['guestAuthHash']
        jira_payload['fields']['customfield_10431']= k['guestCity']
        jira_payload['fields']['customfield_10432']= k['guestCountry']
        jira_payload['fields']['customfield_10433']= k['guestEmail']
        jira_payload['fields']['customfield_10428']= k['guestExternalAccountId']
        jira_payload['fields']['customfield_10426']= k['guestFirstName']
        jira_payload['fields']['customfield_10427']= k['guestLastName']
        jira_payload['fields']['customfield_10425']= k['guestName']
        jira_payload['fields']['customfield_10481']= k['guestNote']
        jira_payload['fields']['customfield_10434']= k['guestPicture']
        jira_payload['fields']['customfield_10418']= k['guestPortal']
        jira_payload['fields']['customfield_10435']= k['guestRecommendations']
        jira_payload['fields']['customfield_10436']= k['guestTrips']
        jira_payload['fields']['customfield_10437']= k['guestWork']
        jira_payload['fields']['customfield_10429']= k['guestZipCode']
        jira_payload['fields']['customfield_10480']= k['hostNote']
        jira_payload['fields']['customfield_10462']= k['hostawayCommissionAmount']
        jira_payload['fields']['customfield_10409']= k['hostawayReservationId']
        jira_payload['fields']['customfield_10448']= k['infants']
        jira_payload['fields']['customfield_10503']= k['insertedOn']
        jira_payload['fields']['customfield_10499']= k['isArchived']
        jira_payload['fields']['customfield_10452']= k['isDatesUnspecified']
        jira_payload['fields']['customfield_10438']= k['isGuestIdentityVerified']
        jira_payload['fields']['customfield_10439']= k['isGuestVerifiedByEmail']
        jira_payload['fields']['customfield_10441']= k['isGuestVerifiedByFacebook']
        jira_payload['fields']['customfield_10442']= k['isGuestVerifiedByGovernmentId']
        jira_payload['fields']['customfield_10443']= k['isGuestVerifiedByPhone']
        jira_payload['fields']['customfield_10444']= k['isGuestVerifiedByReviews']
        jira_payload['fields']['customfield_10440']= k['isGuestVerifiedByWorkEmail']
        jira_payload['fields']['customfield_10420']= k['isInitial']
        jira_payload['fields']['customfield_10422']= k['isInstantBooked']
        jira_payload['fields']['customfield_10421']= k['isManuallyChecked']
        jira_payload['fields']['customfield_10465']= k['isPaid']
        jira_payload['fields']['customfield_10500']= k['isPinned']
        jira_payload['fields']['customfield_10419']= k['isProcessed']
        jira_payload['fields']['customfield_10498']= k['isStarred']
        jira_payload['fields']['customfield_10505']= k['latestActivityOn']
        jira_payload['fields']['customfield_10403']= k['listingMapId']
        jira_payload['fields']['customfield_10404']= k['listingName']
        jira_payload['fields']['customfield_10457']= k['nights']
        jira_payload['fields']['customfield_10445']= k['numberOfGuests']
        jira_payload['fields']['customfield_10424']= k['pendingExpireDate']
        jira_payload['fields']['customfield_10449']= k['pets']
        jira_payload['fields']['customfield_10458']= k['phone']
        jira_payload['fields']['customfield_10453']= k['previousArrivalDate']
        jira_payload['fields']['customfield_10454']= k['previousDepartureDate']
        jira_payload['fields']['customfield_10423']= k['reservationDate']
        jira_payload['fields']['customfield_10502']= k['reservationFees']
        jira_payload['fields']['customfield_10464']= k['securityDepositFee']
        jira_payload['fields']['customfield_10406']= k['source']
        jira_payload['fields']['customfield_10477']= k['status']
        jira_payload['fields']['customfield_10472']= k['stripeGuestId']
        jira_payload['fields']['customfield_10473']= k['stripeMessage']
        jira_payload['fields']['customfield_10460']= k['taxAmount']
        jira_payload['fields']['customfield_10459']= k['totalPrice']
        print(jira_payload)
        jira_payload_new=json.dumps(jira_payload)
        print(jira_payload_new)
        jira_response = requests.request("POST", jira_, headers=jira_headers, data = jira_payload_new)
        print(jira_response.text.encode('utf8'))





pull_HA_push_jira_RD(jira_,HA_token,HA_client_secret,HA_access_token,jira_secret)
