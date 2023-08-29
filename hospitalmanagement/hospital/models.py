from django.db import models
from django.contrib.auth.models import User
import ibm_db



departments=[('Cardiologist','Cardiologist'),
('Dermatologists','Dermatologists'),
('Emergency Medicine Specialists','Emergency Medicine Specialists'),
('Allergists/Immunologists','Allergists/Immunologists'),
('Anesthesiologists','Anesthesiologists'),
('Colon and Rectal Surgeons','Colon and Rectal Surgeons')
]
class Doctor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/DoctorProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=True)
    department= models.CharField(max_length=50,choices=departments,default='Cardiologist')
    status=models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return "{} ({})".format(self.user.first_name,self.department)



class Patient(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/PatientProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    symptoms = models.CharField(max_length=100,null=False)
    assignedDoctorId = models.PositiveIntegerField(null=True)
    admitDate=models.DateField(auto_now=True)
    status=models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name+" ("+self.symptoms+")"


class Appointment(models.Model):
    patientId=models.PositiveIntegerField(null=True)
    doctorId=models.PositiveIntegerField(null=True)
    patientName=models.CharField(max_length=40,null=True)
    doctorName=models.CharField(max_length=40,null=True)
    appointmentDate=models.DateField(auto_now=True)
    description=models.TextField(max_length=500)
    status=models.BooleanField(default=False)



class PatientDischargeDetails(models.Model):
    patientId=models.PositiveIntegerField(null=True)
    patientName=models.CharField(max_length=40)
    assignedDoctorName=models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=True)
    symptoms = models.CharField(max_length=100,null=True)

    admitDate=models.DateField(null=False)
    releaseDate=models.DateField(null=False)
    daySpent=models.PositiveIntegerField(null=False)

    roomCharge=models.PositiveIntegerField(null=False)
    medicineCost=models.PositiveIntegerField(null=False)
    doctorFee=models.PositiveIntegerField(null=False)
    OtherCharge=models.PositiveIntegerField(null=False)
    total=models.PositiveIntegerField(null=False)


def insert_db(firstname,lastname,username,password,address,mobile,symptoms,doctorid,profilepic):
    conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=125f9f61-9715-46f9-9399-c8177b21803b.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=30426;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=gnz67912;PWD=ReQhMGBICOC8744Z", '', '')
    if conn:
        sql= "INSERT into PATIENTSIGNUP VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(firstname,lastname,username,password,address,mobile,symptoms,doctorid,profilepic)
        stmt = ibm_db.exec_immediate(conn, sql)
        return "Number of affected rows: ", ibm_db.num_rows(stmt)
    else:
        return 'Data is not submitted'

def admin_insert(firstname,lastname,username,password):
    conn=ibm_db.connect("DATABASE=bludb;HOSTNAME=125f9f61-9715-46f9-9399-c8177b21803b.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=30426;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=gnz67912;PWD=ReQhMGBICOC8744Z", '', '')
    if conn:
        sql="insert into ADMINSIGNUP VALUES('{}','{}','{}','{}')".format(firstname,lastname,username,password)
        stmt=ibm_db.exec_immediate(conn,sql)
        return "Number of rows effected:",ibm_db.num_rows(stmt)
    else:
        return "Data is not submitted"

def doctor_insert(firstname,lastname,username,password,department,mobile,address,profilepic):
    conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=125f9f61-9715-46f9-9399-c8177b21803b.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=30426;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=gnz67912;PWD=ReQhMGBICOC8744Z", '', '')
    if conn:
        sql= "INSERT into DOCTORSIGNUP VALUES('{}','{}','{}','{}','{}','{}','{}','{}')".format(firstname,lastname,username,password,department,mobile,address,profilepic)
        stmt = ibm_db.exec_immediate(conn, sql)
        return "Number of affected rows: ", ibm_db.num_rows(stmt)
    else:
        return 'Data is not submitted'
    

def book_appointment_insert(description,doctorId):
    conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=125f9f61-9715-46f9-9399-c8177b21803b.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=30426;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=gnz67912;PWD=ReQhMGBICOC8744Z", '', '')
    if conn:
        sql= "INSERT into BOOKAPPOINTMENT VALUES('{}','{}')".format(description,doctorId)
        stmt = ibm_db.exec_immediate(conn, sql)
        return "Number of affected rows: ", ibm_db.num_rows(stmt)
    else:
        return 'Data is not submitted'