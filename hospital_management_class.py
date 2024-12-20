#hospital management system:
#1. patient class(patient private info p-id,pname,gender,contact no.)
#2. doctor class(id,name,specialization)


class patient:
    #__p_id=1
    def __init__(self,p_id,p_name,gender,mob_no):
        self.__p_id=p_id
        self.__p_name=p_name
        self.__gender=gender
        self.__mob_no=mob_no
        #patient.__p_id=patient.__p_id+1
    
    def get_patientdetails(self):
        return{'Patient ID': self.__p_id,
'Patient Name': self.__p_name,
'Gender': self.__gender,
'mobile No.': self.__mob_no}
    
    def set_patientdetails(self,p_id,p_name,gender,mob_no):
        self.__p_id=p_id
        self.__p_name=p_name
        self.__gender=gender
        self.__mob_no=mob_no


class doctor:
    def __init__(self,d_name,d_id,specialization):
        self.__d_name=d_name
        self.__d_id=d_id
        self.__specialization=specialization
    
    def get_doctordetails(self):
        return{'dotor name':self.__d_name,
        'doctor id':self.__d_id,
        'doctor specialization':self.__specialization,}
    
class medicalrecord:
    def __init__(self):
        self.__record={}
    def add_record(self,patient,doctor,diagonis,medication):
        self.__record[patient.get_patientdetails['Patient ID']]={'patient':patient.get_patientdetails(),'doctor':doctor.get_doctordetails(),'diagonis':diagonis,'mdication':medication}

    def getrecord(self):
        return self.__record
        

#main code:
if  __name__ =='__main__':

    patient1=patient(1,'happy','male',8888888888)
    # print(patient1.get_patientdetails()['Patient ID'])

    #patient2=patient(2,'kartik','male',233232)
    # print(patient2.get_patientdetails()['Patient ID'])

    # patient1.set_patientdetails(3,'manmohan','male',19328290382)
    # print(patient1.get_patientdetails())


    doctor1=doctor('manmohan',12,'psycatrist')
    #print(doctor1.get_doctordetails())

    r1=medicalrecord()
    r1.add_record(patient1,doctor1,'leg pain','paracitamol')
    print(r1.getrecord())



    
        