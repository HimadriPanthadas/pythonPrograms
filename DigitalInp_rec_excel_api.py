import gspread
import serial
from oauth2client.service_account import ServiceAccountCredentials

#connecting to arduino
arduino = serial.Serial('com3', 9600)
print('Established serial connection to Arduino')


#connecting client to server
scope=['https://www.googleapis.com/auth/drive']
credentials= ServiceAccountCredentials.from_json_keyfile_name('credentials.json',scope)
client= gspread.authorize(credentials)
sheet=client.open('StakeCalculator').sheet1

#finding the empty row of the excel sheet
empty_row=len(sheet.get_all_records())+1

while True:
    #taking data from the port
    arduino_data = arduino.readline()

    decoded_values = int(arduino_data.decode("utf-8"))
    print(decoded_values)

    #inputting the value in the sheet
    if(decoded_values!=-1):
        empty_row+=1;
        #total_share=input("Please input the total share:\n")
        sheet.update_cell(empty_row,1,10)
        #percentage=input("Please input your percentage:\n")
        sheet.update_cell(empty_row,2,decoded_values);
        '''your_Share=float(percentage)/100*float(total_share)
        sheet.update_cell(empty_row,3,your_Share)
       
        print("Your share is: "+str(your_Share))
        print("\n")'''
    decoded_values=-1


